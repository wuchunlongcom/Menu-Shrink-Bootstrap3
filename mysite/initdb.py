# -*- coding: UTF-8 -*-
import os
import sys
import django
import random

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    django.setup()
    from django.contrib.auth.models import User, Group, Permission
    
    #组添加权限 django==2.2.6 通用
    operatorGroup = Group.objects.create(name='Operator')
    operatorGroup.permissions.add(
        #Permission.objects.get(name='Can add blog'),
              
    )
    operatorGroup.save()
    
    customerGroup = Group.objects.create(name='Customer')
    customerGroup.permissions.add()
    customerGroup.save()
        
    isname = User.objects.filter(username = 'admin')
    if isname:
        user = User.objects.get(username='admin')
        user.set_password('admin')
        user.save()
    else:
        User.objects.create_superuser('admin', 'admin@test.com','admin')
     

