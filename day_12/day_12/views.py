from django.template import RequestContext 
from django.shortcuts import render_to_response
from django.db import models
from day_12.models import lang
from day_12.models import stu
from day_12.models import writ, students
from day_12.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login ,logout
from django.http import HttpResponse

def home(request):
	ctx=RequestContext(request)
	temp_name="index.html"
	response= render_to_response(temp_name,{},ctx)

	return response

def aboutus(request):
	ctx=RequestContext(request)
	temp_name="about.html"
	response= render_to_response(temp_name,{},ctx)
	return response

def blog(request):
	ctx=RequestContext(request)
	temp_name="blog.html"
	response= render_to_response(temp_name,{},ctx)
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

def forms(request):
	ctx=RequestContext(request)
	temp_name="forms.html"
	response = render_to_response(temp_name,locals(),ctx)
	return response

def formsubmit(request):
	if request.method=="POST":
		name=request.POST.get("name")
		email=request.POST.get("email")
		phone=request.POST.get("phone")
		query=request.POST.get("query")
		print name, email, phone, query
		e=Enquiry()
		e.name=name
		e.email=email
		e.phone=phone
		e.query=query
		e.save()
		temp_name="formsubmit.html"
	else:
		temp_name="forms.html"
	ctx=RequestContext(request)
	response = render_to_response(temp_name,locals(),ctx)
	return response

def form1(request):
	ctx=RequestContext(request)
	temp_name="form1.html"
	response = render_to_response(temp_name,locals(),ctx)
	return response

def formsubmit1(request):
	if request.method=="POST":
		course=request.POST.get("course")
		idea=request.POST.get("idea")
		assit=request.POST.get("assit")
		fileupload=request.POST.get("fileupload")
		print course, idea, assit, fileupload
		f=feedback()
		f.course=course
		f.idea=idea
		f.assit=assit
		f.fileupload=fileupload
		f.save()
		temp_name="formsubmit1.html"
	else: 
		temp_name="form1.html"
	ctx=RequestContext(request)
	response = render_to_response(temp_name,locals(),ctx)
	return response

def login1(request):
	myuser="vb.anurag"
	mypass="1503#@2101"
	user=authenticate(username=myuser,password=mypass)
	print user
	temp_name="mylogin.html"
	ctx=RequestContext(request)
	response = render_to_response(temp_name,locals(),ctx)
	return response
	
def logout1(request):
	logout(request)
	temp_name="mylogin.html"
	ctx=RequestContext(request)
	response = render_to_response(temp_name,locals(),ctx)
	return response



def signup(request):
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
		

		#if User.objects.get(username=email):

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
		#else:
		#	temp_name="signup.html"

		temp_name="login_cumplete.html"
	else:
		temp_name="signup.html"
	ctx=RequestContext(request)
	response = render_to_response(temp_name,locals(),ctx)
	return response



def login_submit(request):
	ctx=RequestContext(request)
	temp_name="signup.html"
	response = render_to_response(temp_name,locals(),ctx)
	return response



def display(request, myval):
	return HttpResponse(myval)




def login_project(request):
	if request.method=="POST":
		myuser=request.POST.get(user_name)
		mypass=request.POST.get(user_pass)
		user=authenticate(username=myuser,password=mypass)
		print user
		temp_name="login_cumplete.html"
	else:
		temp_name="login.html"
	ctx=RequestContext(request)
	response = render_to_response(temp_name,locals(),ctx)
	return response
	
def logout_project(request):
	logout(request)
	temp_name="login.html"
	ctx=RequestContext(request)
	response = render_to_response(temp_name,locals(),ctx)
	return response











	