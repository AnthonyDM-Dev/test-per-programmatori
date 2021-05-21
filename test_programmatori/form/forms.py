from django import forms
from django.conf import settings

class ProfileForm(forms.Form):
	STUDY_TITLE_CHOICES = [
		("Diploma", 'Diploma'),
		("Laurea", 'Laurea'),
	]
	name = forms.CharField(label="Nome")
	surname = forms.CharField(label="Cognome")
	email = forms.EmailField()
	phone = forms.IntegerField(label="Numero di telefono")
	date_of_birth = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, label="Data di nascita (formato gg/mm/aa)")
	study_title = forms.ChoiceField(choices=STUDY_TITLE_CHOICES, label="Titolo di studi")
	curriculum = forms.FileField(widget=forms.FileInput(attrs={'class':'file-custom'}))

	def clean(self):
		cleaned_data = super().clean()
		name = self.cleaned_data.get('name')
		surname = self.cleaned_data.get('surname')
		email = self.cleaned_data.get('email')
		phone = self.cleaned_data.get('phone')
		date_of_birth = self.cleaned_data.get('date_of_birth')
		study_title = self.cleaned_data.get('study_title')
		curriculum = self.cleaned_data.get('curriculum')
		#Phone checking
		if len(str(phone)) > 10:
			raise forms.ValidationError('Phone number not valid.')
		#CV format checking
		cv_format = str(curriculum)[-4:]
		allowable_formats = [".pdf", ".doc"]
		if cv_format not in allowable_formats:
			raise forms.ValidationError('')
		print("CLEANED DATA: ", cleaned_data)
		return cleaned_data