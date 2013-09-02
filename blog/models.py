from django.db import models
from thumbs import ImageWithThumbsField

# Create your models here.

class Blog(models.Model):

	title = models.CharField(max_length = 120)
	pub_date = models.DateTimeField()
	is_verticle = models.BooleanField(verbose_name = 'Is the images verticle?')

	def __unicode__(self):
		return self.title

def upload_to(instance, filename):
	return 'blog/%d/%s'%(instance.blog.id,filename)


class Image(models.Model):
	title = models.CharField(max_length = 120)
	image = ImageWithThumbsField(upload_to = upload_to,sizes = ((180,270),(260,180),(800,600),(400,600)))
	blog = models.ForeignKey(Blog)
	is_thumb = models.BooleanField(verbose_name = 'set to thumb')
	is_verticle = models.BooleanField(verbose_name = 'is the image verticle?')
	def __unicode__(self):
		return self.title