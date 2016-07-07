from django.db import models

# deals with database # dealing with forms and db.
# Create your models here.

class SignUp(models.Model):
	# model fields
	email = models.EmailField()
	full_name = models.CharField(max_length = 120 ,blank = True, null = True)
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)

	def __unicode__(self):
		return self.email

	def __str__(self): # for python 3 # this
		return self.email