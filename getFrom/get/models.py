from django.db import models

class Our_database(models.Model):
	"""docstring for Our_database"""
	url = models.CharField(max_length=200)

class Transition(models.Model):
	url_id = models.CharField(max_length=5)
	url = models.CharField(max_length=200)
	time = models.CharField(max_length=100)
