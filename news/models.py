from django.db import models

# Create your models here.
class Reporter(models.Model):
	full_name = models.CharField(max_length=20)
	def __unicode__(self):
		return self.full_name
		
class Article(models.Model):
	reporter = models.ForeignKey(Reporter)
	pub_date = models.DateTimeField()
	headline = models.CharField(max_length=40)
	content = models.TextField()
	views_count = models.IntegerField(default=0)
	def __unicode__(self):
		return self.headline
	