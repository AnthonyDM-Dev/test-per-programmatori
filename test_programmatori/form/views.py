from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render
from django.utils import timezone
# Other imports
import requests, json
from datetime import timedelta
# From this app
from .models import Profile, Job
from .forms import ProfileForm

# Create your views here.
def form_view(request):
	form = ProfileForm()
	queryset_to_render = Job.objects.all()
	print("GET REQUEST HERE: ", request.GET)
	print("POST REQUEST HERE: ", request.POST)
	print("FILES REQUEST HERE: ", request.FILES)

	if request.method == 'POST':
		# reCaptcha verification
		cap_token = request.POST.get('g-recaptcha-response')
		cap_url = "https://www.google.com/recaptcha/api/siteverify"
		cap_secret = "6Lf7Tt0aAAAAAHech2hM8XCKzOJHNCai3vUbOJP7"
		cap_data = {"secret": cap_secret, "response": cap_token}
		cap_server_response = requests.post(url=cap_url, data=cap_data)
		cap_json = json.loads(cap_server_response.text)
		if cap_json['success'] == True:

			form = ProfileForm(request.POST or None, request.FILES or None)
			print(form.is_valid())
			if form.is_valid():

				# Profile creation
				name = form.cleaned_data.get('name')
				surname = form.cleaned_data.get('surname')
				email = form.cleaned_data.get('email')
				phone = form.cleaned_data.get('phone')
				date_of_birth = form.cleaned_data.get('date_of_birth')
				study_title = form.cleaned_data.get('study_title')
				curriculum = form.cleaned_data.get('curriculum')
				profile = Profile.objects.create(name=name,
												 surname=surname,
												 email=email,
												 phone=phone,
												 date_of_birth=date_of_birth,
												 study_title=study_title,
												 curriculum=curriculum,
												 )

				# Associazione del profilo ai lavori a cui si è candidato
				role = request.POST.get('role')
				location = request.POST.get('location')
				duty_list = []
				for d in request.POST.getlist(f'{role}-{location}'):
					duty_list.append(d)
				if location == "Anyone":
					jobs_queryset = Job.objects.filter(role=role, duty__in=duty_list)
				else:
					jobs_queryset = Job.objects.filter(role=role, location=location, duty__in=duty_list)
				for job in jobs_queryset:
					profile.job.add(job)
					profile.save()
				messages.success(request, "Congratulations, form submitted!")
			else:
				messages.error(request, 'The input data you entered are not correct.')
		else:
			messages.error(request, 'You did not pass the reCaptcha verification. Please, try again.')
	return render(request, 'form_view.html', {"form": form,
											  "queryset": queryset_to_render,
											  }
				  )

@login_required(login_url="/admin/login/?next=/staff/")
def staff_view(request):
	profiles = Profile.objects.all().filter().order_by('name')
	queryset_n_profiles = []
	counting = 0
	search = False
	print("GET REQUEST RESULTS: ", request.GET.get)
	query_request = request.GET.get('submit')

	# Creation of filters
	if query_request:
		role = request.GET.get('role')
		study_title = request.GET.get('study_title')
		location = request.GET.get('location')

		# Age filter
		range = request.GET.get('range')
		today = timezone.now()
		if range == '':
			max_range_date = today - timedelta(days=365 * 100)
			min_range_date = today
		else:
			min_range_days = int(range[:2]) * 365
			max_range_days = int(range[2:]) * 365
			min_range_date = today - timedelta(days=min_range_days)
			max_range_date = today - timedelta(days=max_range_days)

		# Profile filter application
		profiles = Profile.objects.filter(job__role__icontains=role,
										  job__location__icontains=location,
										  study_title__icontains=study_title,
										  date_of_birth__range=[max_range_date, min_range_date]
										  ).distinct()
		print("PROFILES FILTERED: ", profiles)
		search = True
		counting = profiles.count()
	for x in profiles:
		n_profiles = len(Profile.objects.all().filter())
		queryset_n_profiles.append(n_profiles)
	table = dict(zip(profiles, queryset_n_profiles))
	return render(request, 'admin_view.html', {'table': table,
											   'counting': counting,
											   'search': search})