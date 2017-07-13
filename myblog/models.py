from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length = 50)
	image = models.ImageField(upload_to = 'myblog/image/post', default = None)
	content = models.TextField()
	published_date = models.DateTimeField(default = timezone.now)

	def __str__(self):
		return self.title


class Project(models.Model):
	title = models.CharField(max_length = 50)
	link = models.URLField()
	image = models.ImageField(upload_to = 'myblog/image/project', default = None)
	detail = models.TextField()
	created_on = models.DateTimeField()


	def __str__(self):
		return self.title


class SocialSite(models.Model):
	site_name = models.CharField(max_length = 10)
	link = models.URLField()


	class Meta:
		verbose_name_plural = 'Social Sites'

	def __str__(self):
		return self.site_name


class Contact(models.Model):
	message_from_me = models.TextField()
	subject = models.CharField(max_length = 33)
	message_from_user = models.TextField()


	def __str__(self):
		return self.subject

	class Meta:
		verbose_name_plural = 'Contact'


class About(models.Model):
	about_me = models.TextField()


	class Meta:
		verbose_name_plural = 'About'
