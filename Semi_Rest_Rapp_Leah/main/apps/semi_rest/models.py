from __future__ import unicode_literals


# Create your models here.from __future__ import unicode_literals
from django.db import models
import re

class UserManager(models.Manager):
    def basic_validator(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        errors={}
        if len(postData["first_name"])<1:
            errors["first_name"] = "Please Enter First Name"
        if len(postData["last_name"])<1:
            errors["last_name"] = "Please Enter Last Name"
        if len(postData["email"])<1:
            errors["email"] = "Please Enter Email"
        if not EMAIL_REGEX.match(postData["email"]):
            errors["email"]="Please Enter Valid Eamil Address"
        return errors

class Users(models.Model):
     id = models.AutoField(primary_key = True)
     first_name = models.CharField(max_length=255)
     last_name = models.CharField(max_length=255)
     email=models.TextField(blank=True)
     created_at = models.DateTimeField(auto_now_add = True)
     updated_at = models.DateTimeField(auto_now = True)

     objects=UserManager()
     
     






