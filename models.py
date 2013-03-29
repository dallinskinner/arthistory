from django.db import models

class Artwork(models.Model):
	artist = models.ForeignKey('Artist')
	category = models.ForeignKey('Category')
	year = models.IntegerField()
	title = models.CharField(max_length=50)
	image = models.ImageField(upload_to='uploads')
	description = models.TextField(null=True, blank=True)
	unit = models.IntegerField()
	def __unicode__(self):
		return self.title

class Artist(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField(null=True, blank=True)
	def __unicode__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField(null=True, blank=True)
	def __unicode__(self):
		return self.name

class Term(models.Model):
	term = models.CharField(max_length=50)
	description = models.TextField(null=True, blank=True)
	def __unicode__(self):
		return self.term