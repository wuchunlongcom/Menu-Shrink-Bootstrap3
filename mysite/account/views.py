# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponse,\
    StreamingHttpResponse
from django.contrib.auth.decorators import login_required 




def index0(request):           
    return render(request, 'mobile-phone/index0.html', context=locals()) 

def index1(request):           
    return render(request, 'mobile-phone/index1.html', context=locals()) 

def index2(request):           
    return render(request, 'mobile-phone/index2.html', context=locals()) 

def index3(request):           
    return render(request, 'mobile-phone/index3.html', context=locals()) 

def index4(request):           
    return render(request, 'mobile-phone/index4.html', context=locals()) 

def index5(request):           
    return render(request, 'mobile-phone/index5.html', context=locals()) 


#-----------------------------------------------------------------#

# http://localhost:8000/ 
def index(request):           
    return render(request, 'home/index.html', context=locals()) 


def progress(request):           
    return render(request, 'home/progress.html', context=locals()) 

def table(request):           
    return render(request, 'home/table.html', context=locals()) 

def img(request):           
    return render(request, 'home/img.html', context=locals()) 


#@login_required
def bar_chart(request):           
    return render(request, 'home/bar_chart.html', context=locals()) 

def bar_chart2(request):           
    return render(request, 'home/bar_chart2.html', context=locals()) 


   