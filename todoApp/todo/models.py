from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Project(models.Model):
	project_name = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

class Task(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	task_name = models.CharField(max_length=200)
	completed = models.BooleanField(default=False)