from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.db import models
from django.utils import timezone
import datetime
from .models import Course,Video,Document
from django.urls import reverse
#from .forms import ExtractAllDataForm, LoginForm,ViewDeliveryOutForm, ManagerForm,Delivery_OutForm,ViewClientForm, ViewDeliveryInForm, ClientForm, Delivery_InForm, BillForm
from datetime import date as DATE
from django.shortcuts import render
from django.shortcuts import get_object_or_404 
import json
from django.http import HttpResponse
from django.views.generic.edit import UpdateView
# Create your views here.

def index(request):
	return render(request,'index.html',)

def course_list(request, discipline="telecom"):
	courses=Course.objects.all()
	return render(request, 'course_list.html', {'courses':courses, 'discipline':discipline})

def course_prompt(request, name):
	return render(request,'course_prompt.html', {'name':name})

def course_videos(request, name):
	videos = Video.objects.all().filter(Course=name)
	return render(request,'course_videos.html',{ 'videos':videos , 'name':name})

def course_documents(request, name):
	documents = Document.objects.all().filter(Course=name)
	siz = documents.count()
	data = dict()
	for  i in range(1,siz+1):
		data[i]=documents[i-1]

	return render(request,'course_documents.html',{'data':data, 'name':name, })
