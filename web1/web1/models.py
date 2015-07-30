from django.db import models
from django.contrib.auth.models import User

	
class Enquiry(models.Model):
	name=models.CharField(max_length=100, null=False, blank=False)
	phone=models.BigIntegerField()
	email=models.EmailField(null=False,blank=False)
	query=models.CharField(max_length=200, null=False, blank=False)
	timestamp=models.DateTimeField(auto_now=True)
	is_active=models.BooleanField(default=True)
	
	def __unicode__(self):
		return self.email + str(self.phone)
  
#Helping hand

class helping_hand(models.Model):
	name_project=models.CharField(max_length=25, null=False, blank=False)
	idea=models.CharField(max_length=30, null=False, blank=False)
	email=models.EmailField()
	assit=models.CharField(max_length=40)
	cost=models.BigIntegerField()
	description=models.CharField(max_length=500, null=False, blank=False)
	fileupload=models.FileField(upload_to="blueprint/")

#BAtti Jalao form

class batti_jalao(models.Model):
	course_name=models.CharField(max_length=15, null=False, blank=False)
	email_id=models.EmailField()
	idea=models.CharField(max_length=20,null=False, blank=False)
	type_of_assis=models.CharField(max_length=20)
	project_copy=models.FileField(upload_to="batti_jalao_projct/")

#user Registration form

class user_reg(models.Model):
	user=models.ForeignKey(User)
	college_name=models.CharField(max_length=30, null=False, blank=False)
	course_name=models.CharField(max_length=20, null=False, blank=False)
	_sem_yr=models.IntegerField(null=False, blank=False)
	_country=models.CharField(max_length=15, null=False, blank=False)


# Projects Class


class all_project(models.Model):
	project_title=models.CharField(max_length=100, null=False, blank=False)
	project_class=models.CharField(max_length=100, null=False, blank=False)
	project_desc=models.CharField(max_length=1000, null=False, blank=False)
	project_image=models.ImageField(upload_to="project_image/")
	project_price=models.BigIntegerField()

class project_undergrad(models.Model):
	project=models.ForeignKey(all_project)
	project_Divison=models.CharField(max_length=30, null=False, blank=False)

class project_postgrad(models.Model):
	project=models.ForeignKey(all_project)
	project_Divison=models.CharField(max_length=30, null=False, blank=False)

class project_research(models.Model):
	project=models.ForeignKey(all_project)
	project_Divison=models.CharField(max_length=15, null=False, blank=False)


#expert panel contact form

class expert_panel(models.Model):
	name=models.CharField(max_length=50, null=False, blank=False)
	email=models.EmailField()
	subject=models.CharField(max_length=50, null=False, blank=False)
	message=models.CharField(max_length=2000, null=False, blank=False)



