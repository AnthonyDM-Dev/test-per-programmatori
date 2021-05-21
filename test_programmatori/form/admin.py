from django.contrib import admin
from .models import Profile, Job

class ProfileAdmin(admin.ModelAdmin):
	list_display = ('name', 'surname', 'email', 'date_of_birth')

class JobAdmin(admin.ModelAdmin):
	list_display = ('role', 'duty', 'description', 'location')

# Register your models here.
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Job, JobAdmin)