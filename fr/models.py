from django.db import models

# Create your models here.

class mosque_main(models.Model):
	country = models.CharField(max_length=100)
	city = models.CharField(max_length=1000)
	borough = models.CharField(max_length=1000)
	area = models.CharField(max_length=1000)
	name = models.CharField(max_length=1000)
	address = models.CharField(max_length=1000)
	postcode = models.CharField(max_length=1000)
	website = models.CharField(max_length=1000)