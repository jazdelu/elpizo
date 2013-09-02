from django.db import models

# Create your models here.

class Lookbook(models.Model):

	name = models.CharField(max_length = 120)
	lookbook = models.ImageField(upload_to = 'lookbook/')
	thumbnail = models.ImageField(upload_to = 'lookbook/')
	rollover = models.ImageField(upload_to = 'lookbook/')
	description = models.TextField(blank=True)
	pub_date = models.DateTimeField(auto_now_add = True, editable = False)

	def __unicode__(self):
		return self.name