from django.db import models

# Create your models here.
class User(models.Model):
	username = models.CharField(u'用户名', max_length=64, unique=True)
	password = models.CharField(u'密码', max_length=32)
	
	def __unicode__(self):
		return self.username