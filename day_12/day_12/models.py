from django.db import models
from django.contrib.auth.models import User

class lang(models.Model):
	lang_name= models.CharField (max_length=20)
	score = models.IntegerField (max_length=2)

	def __unicode__(self):
		return self.lang_name

class stu(models.Model):
	stu_name =models.CharField(max_length=40)
	stu_course = models.CharField(max_length=40)
	stu_des=models.CharField(max_length=40)

	def __unicode__ (self):
		return self.stu_name

class writ(models.Model):
	langs=models.ForeignKey(lang)
	name= models.CharField(max_length=20)
	book=models.CharField(max_length=20)

	def __unicode__(self):
		return self.name

class students(models.Model):
	name=models.CharField(max_length=10)
	DOB=models.DateField()
	email=models.EmailField()
	phone=models.BigIntegerField(max_length=20)

	def __unicode__(self):
		return self.name

class Accounts(models.Model):
	user =models.ForeignKey(User)
	photo=models.ImageField(upload_to="pic/")
	profession=models.CharField(max_length=20)

	def __unicode__(self):
		return self.profession

	
class Enquiry(models.Model):
	name=models.CharField(max_length=100, null=False, blank=False)
	phone=models.BigIntegerField()
	email=models.EmailField(null=False,blank=False)
	query=models.CharField(max_length=200, null=False, blank=False)
	timestamp=models.DateTimeField(auto_now=True)
	is_active=models.BooleanField(default=True)
	
	def __unicode__(self):
		return self.email + str(self.phone)

class feedback(models.Model):
	course=models.CharField(max_length=25, null=False, blank=False)
	idea=models.BooleanField()
	assit=models.CharField(max_length=40)
	fileupload=models.FileField(upload_to="blueprint/")

class user_reg(models.Model):
	user=models.ForeignKey(User)
	college_name=models.CharField(max_length=30, null=False, blank=False)
	course_name=models.CharField(max_length=20, null=False, blank=False)
	_sem_yr=models.IntegerField(null=False, blank=False)
	_country=models.CharField(max_length=15, null=False, blank=False)
	


