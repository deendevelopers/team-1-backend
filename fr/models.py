from django.db import models

# Create your models here.

class mosque_main(models.Model):
	country = models.CharField(max_length=100)
	city = models.CharField(max_length=1000)
	borough = models.CharField(max_length=1000)
	area = models.CharField(max_length=1000)
	name = models.CharField(max_length=1000)
	postcode = models.CharField(max_length=1000)
	website = models.CharField(max_length=1000)

class Mosque_Comment(models.Model):
	user_id = models.CharField(max_length=100)
	mosque_id = models.CharField(max_length=100)
	category_name = models.CharField(max_length=100)
	comment = models.CharField(max_length=10000)
	comment_type = models.CharField(max_length=100)
	timestamp = models.DateTimeField(auto_now_add=True)