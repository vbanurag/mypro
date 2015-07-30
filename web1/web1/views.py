﻿from django.template import RequestContext 
from django.shortcuts import render_to_response
from django.db import models
from web1.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login ,logout
from django.http import HttpResponse


#home page of website

def home(request):
	ctx=RequestContext(request)
	temp_name="index.html"
	response= render_to_response(temp_name,{},ctx)

	return response


# expert panel of page

def contact_us(request):
	if request.method=="POST":
		name=request.POST.get("name")
		email=request.POST.get("email")
		subject=request.POST.get("subject")
		message=request.POST.get("message")
		print name, email, subject, message
		
		e_p=expert_panel()

		e_p.name=name
		e_p.email=email
		e_p.subject=subject
		e_p.message=message
		e_p.save()
		temp_name="contact-us.html"
	else: 
		temp_name="contact-us.html"
	ctx=RequestContext(request)
	response = render_to_response(temp_name,locals(),ctx)
	return response



def foer(request):
	ctx=RequestContext(request)
	temp_name="foer.html"
	values=lang.objects.all()

	hval = [hstart for hstart in values if hstart.lang_name.startswith("h") or hstart.lang_name.startswith("H")]
	print hval
	stu_val=stu.objects.all()
	writer=writ.objects.all()
	st=students.objects.all()
	ac=Accounts.objects.all()
	print hval
	print st
	print writer
	print stu_val
	print values
	print ac
	e= Enquiry()
	e.name="myname"
	e.email="ada@gmail.com"
	e.phone=1224456788
	e.query="wedfsdgdsfhgfsh"
	e.save()
	response = render_to_response(temp_name,locals(),ctx)
	return response








#login portal of page

def login_project(request):
	if request.method=="POST":
		
		myuser=request.POST.get("user_name")
		mypass=request.POST.get("user_pass")
		user=authenticate(username=myuser, password=mypass)

		if user is not None:
			login(request, user)
			temp_name="index.html"

			#user_ac=user_reg.objects.filter(user__username = request.user.username)

		else:
			temp_name="login.html"
	else:	
		temp_name="login.html"
	ctx=RequestContext(request)
	response = render_to_response(temp_name,locals(),ctx)
	return response



def logout_project(request):
	logout(request)
	temp_name="index.html"
	ctx=RequestContext(request)
	response = render_to_response(temp_name,locals(),ctx)
	return response



def user_signup(request):
	if request.method=="POST":
		first_name=request.POST.get("first_name")
		last_name=request.POST.get("last_name")
		email=request.POST.get("email")
		password=request.POST.get("password")
		_sem_year=request.POST.get("_sem_year")
		country=request.POST.get("country")
		college_name=request.POST.get("college_name")
		course_name=request.POST.get("course_name")
		print first_name, last_name, country, college_name, course_name, _sem_year, email, password
		

		newuser = User.objects.filter(username = email)
		if newuser:
			msg = "User already exists"
		else:
			# create usr here



			u=User()
			u.first_name=first_name
			u.email=email
			u.last_name=last_name
			u.set_password(password)
			u.username=email
			u.save()

			r=user_reg()
			r.user=u
			r.college_name=college_name
			r.course_name=course_name
			r._sem_yr=_sem_year
			r._country=country

			r.save()
			

			temp_name="login.html"
	else:
		temp_name="signup.html"
	ctx=RequestContext(request)
	response = render_to_response(temp_name,locals(),ctx)
	return response


def user_page(request):
	ctx=RequestContext(request)
	temp_name="user.html"
	response= render_to_response(temp_name,{},ctx)
	return response


def signup(request):
	ctx=RequestContext(request)
	temp_name="signup.html"
	response = render_to_response(temp_name,locals(),ctx)
	return response

#End of login project



# creative form of page

def battijalao_form(request):
	if request.method=="POST":
		course_name=request.POST.get("course_name")
		idea=request.POST.get("idea")
		type_of_assis=request.POST.get("type_of_assis")
		email_id=request.POST.get("email_id")
		project_copy=request.POST.get("project_copy")
		print course_name, idea, type_of_assis, project_copy
		
		b=batti_jalao()

		b.course_name=course_name
		b.email_id=email_id
		b.idea=idea
		b.type_of_assis=type_of_assis
		b.project_copy=project_copy
		b.save()
		temp_name="battijalao.html"
	else: 
		temp_name="battijalao.html"
	ctx=RequestContext(request)
	response = render_to_response(temp_name,locals(),ctx)
	return response

#def helpinghand(request):
#	ctx=RequestContext(request)
#	temp_name="helpinghand.html"
#	response = render_to_response(temp_name,locals(),ctx)
#	return response


def helpinghand_form(request):
	if request.method=="POST":
		name_project=request.POST.get("name_project")
		idea=request.POST.get("idea")
		assist=request.POST.get("assist")
		email=request.POST.get("email")
		cost=request.POST.get("cost")
		description=request.POST.get("description")
		fileupload=request.POST.get("fileupload")
		print name_project,cost, idea, assist, email,description

		h=helping_hand()

		h.name_project=name_project
		h.idea=idea
		h.assit=assist
		h.cost=cost
		h.description=description
		h.email=email
		h.fileupload=fileupload
		h.save()
		#
		temp_name="helpinghand.html"
	else: 
		temp_name="helpinghand.html"
	ctx=RequestContext(request)
	response = render_to_response(temp_name,locals(),ctx)
	return response

# end of form

#project categories views


def project(request):
	ctx = RequestContext(request)
	temp_name ="project.html"
	response = render_to_response(temp_name, {} ,ctx)
	return response


def project_bsc(request):
	ctx=RequestContext(request)
	temp_name="project_bsc.html"
	pro=all_project.objects.all()
	pro_bsc=project_undergrad.objects.filter(project_Divison="B.Sc")
	print pro
	print pro_bsc
	response= render_to_response(temp_name,locals(),ctx)
	return response

def project_btech(request):
	ctx=RequestContext(request)
	temp_name="project_btech.html"
	pro=all_project.objects.all()
	pro_btech=project_undergrad.objects.filter(project_Divison="B.Tech")
	print pro
	print pro_btech
	response= render_to_response(temp_name,locals(),ctx)
	return response

def project_detail(request):
	ctx=RequestContext(request)
	temp_name="project_detail.html"
	pro=all_project.objects.all()
	pro_bca=project_undergrad.objects.filter(project_Divison="BCA")
	print pro
	print pro_bca
	response= render_to_response(temp_name,locals(),ctx)
	return response

def project_mca(request):
	ctx = RequestContext(request)
	pro=all_project.objects.all()
	pro_mca=project_postgrad.objects.filter(project_Divison="MCA")
	print pro
	print pro_mca
	temp_name ="project_mca.html"
	response = render_to_response(temp_name, locals() ,ctx)
	return response

def project_desc(request, myvalue):
	ctx=RequestContext(request)
	pro_mca=project_postgrad.objects.filter(id=myvalue)
	
	temp_name="project_desc.html"
	
	response= render_to_response(temp_name,locals(),ctx)
	return response

def project_desc_undergrad(request, myvalue):
	ctx=RequestContext(request)
	pro_mca=project_undergrad.objects.filter(id=myvalue)
	
	temp_name="project_desc.html"
	
	response= render_to_response(temp_name,locals(),ctx)
	return response

def project_desc_ri(request, myvalue):
	ctx=RequestContext(request)
	pro_mca=project_research.objects.filter(id=myvalue)
	
	temp_name="project_desc.html"
	
	response= render_to_response(temp_name,locals(),ctx)
	return response

def project_res(request):
	ctx=RequestContext(request)
	temp_name="project_res.html"
	pro=all_project.objects.all()
	pro_mca=project_research.objects.filter(project_Divison="R&I")
	print pro
	print pro_mca
	response= render_to_response(temp_name,locals(),ctx)
	return response

def project_mtech(request):
	ctx=RequestContext(request)
	temp_name="project_mtech.html"
	pro=all_project.objects.all()
	pro_mtech=project_postgrad.objects.filter(project_Divison="M.TECH")
	print pro
	print pro_mtech
	response= render_to_response(temp_name,locals(),ctx)
	return response




#def project_display(request, myvalue):
#	temp_name="project_desc.html"
#	clas=project_postgrad.object.get(id=p_id)
#	v=all_project.objects.filter(project_class=id)
#	ctx=RequestContext(request)
#	response=render_to_response(temp_name,locals(),ctx)
#	return response







	
