# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [  
    url(r'^progress/$', views.progress, name='progress'),
    url(r'^img/$', views.img, name='img'),
    url(r'^table/$', views.table, name='table'),         
    url(r'^bar/chart/$', views.bar_chart, name='bar_chart'), 
    url(r'^bar/chart2/$', views.bar_chart2, name='bar_chart2'),
    url(r'index0/$', views.index0, name='index0'),   #必须放在最后
    url(r'', views.index, name='index'),   #必须放在最后
]
