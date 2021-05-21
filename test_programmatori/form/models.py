from django.db import models

# Create your models here.

class Job(models.Model):
	role = models.CharField(max_length=50)
	duty = models.CharField(max_length=50)
	description = models.TextField(max_length=500, null=True)
	location = models.CharField(max_length=50)


class Profile(models.Model):
	STUDY_TITLE_CHOICES = [
		("Diploma", 'Diploma'),
		("Laurea", 'Laurea'),
	]
	name = models.CharField(max_length=255, blank=False, default="")
	surname = models.CharField(max_length=255, blank=False, default="")
	email = models.EmailField(max_length=255, blank=False, default="")
	phone = models.IntegerField(blank=False, default="")
	date_of_birth = models.DateTimeField(blank=False, default="")
	study_title = models.CharField(max_length=7, choices=STUDY_TITLE_CHOICES, default="")
	curriculum = models.FileField(upload_to="uploads")
	job = models.ManyToManyField(Job)