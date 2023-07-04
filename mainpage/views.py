from django.shortcuts import render
from unicodedata import category
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Project, Certificate, Contact, Reviews
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator
import json
from django.http import JsonResponse, HttpResponse

import datetime
from datetime import date, timedelta


import csv
from django.template.loader import render_to_string

import tempfile
from django.db.models import Sum

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from django.views import View
from django.http import FileResponse
import os
from django.http import HttpResponseNotFound 
from django.views import generic
from django.urls import reverse_lazy
from .forms import ContactForm
from django.core.mail import send_mail
from .email_utils import send_email





# Create your views here.

def dashboard(request):
    all_items = Project.objects.order_by('-id')
    contacts = Contact.objects.all()
    reviews = Reviews.objects.order_by('-id')
    form = ContactForm()
    email = None
    content = None
    recipient = None
    
    
    context={
        'all_items' : all_items ,
        'contacts' : contacts ,
        'reviews' : reviews,
        'form' : form,
    }
    if request.method == 'POST':
        
        email = request.POST['email']
        content = request.POST['content']
        recipient = 'philipboluwatife0@gmail.com'
    
    
        send_email(email, recipient, content)
       
        
        
    else:
        
        messages.success(request, 'email sent succesfully')

    
    send_email(email, recipient, content)
    
   
    return render(request,'project/dashboard.html', context, )














def add_project(request):
    categories = Category.objects.all()
   
    context ={
        'categories': categories,
    }

    if request.method == 'GET':
        return render(request, 'project/add_project.html', context)
    

    if request.method == 'POST':
        name = request.POST['name']
        link = request.POST['link']
        date = request.POST['date']
        category = request.POST.get('category')
        description = request.POST['description']
        content = request.POST['content']
        image = request.FILES.get('image')

        if not category:
            messages.error(request,'category is required')
            return render(request, 'project/add_category.html', context)
        
        if not name:
            messages.error(request,'Title is required')
            return render(request, 'project/add_project.html', context )
        
        if not link:
            messages.error(request,'link is required')
            return render(request, 'project/add_project.html', context )
        
        if not date:
            messages.error(request,'Published date is required')
            return render(request, 'project/add_project.html', context )
        
        if not description:
            messages.error(request,'description is required')
            return render(request, 'project/add_project.html', context)
        
        if not content:
            messages.error(request,'Content is required')
            return render(request, 'project/add_project.html',  context)
        
        
        
        
        
    Project.objects.create(owner=request.user, name=name, link=link, date=date,
                               category=category, description=description, content=content, image=image)
    messages.success(request, 'Project saved succesfully')
    return redirect('dashboard')




def add_category(request):
    category = Category.objects.all()
   
    context = {
       
        'category': category,
        
        
        
    }
   
    if request.method == 'GET':
        return render(request, 'project/add_category.html', context)
    
    if request.method == 'POST':
        name = request.POST['name']

        if not Category.objects.filter(name=name).exists():
        
            if not name:
                messages.error(request,'category is required')
                return render(request, 'project/add_category.html', context)
            
        else:
                messages.error(request,'CATEGORY already exists')
                return render(request, 'project/add_category.html', context)
        
        Category.objects.create(owner=request.user,
                               name=name)
        messages.success(request, 'Category saved succesfully')
        return redirect('dashboard')
    

def category_view(request, cats):
    category_project = Project.objects.filter(category=cats.replace('-', ''))
    context = {
        'category_project': category_project,
        'cats': cats.replace('-', ''),
        
        
        
    }
    if category_project.exists():
        return render(request, 'project/categories.html', context)
    else:
        
        return render(request, 'project/project.html', context)
    
    
def UploadView(request):
    all_items = Project.objects.all()
    certify = Certificate.objects.order_by('id')
    
    
    
    context={
        'all_items' : all_items ,
        'files' : certify,
    }
    return render(request,'project/pdf.html', context)





    




