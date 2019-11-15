from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.
# class University(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#     department = models.CharField(max_length=100, unique=True)
#     grade = models.IntegerField()

class License(models.Model):
    name = models.CharField(max_length=200,null=True)

class Category(models.Model):
    name = models.CharField(max_length=200,null=True)
    code_no = models.CharField(max_length=200,null=True)

class Student(models.Model):
    title = models.CharField(max_length=200,null=True,default="")
    author = models.ForeignKey(User,on_delete=True,null=True,default=1)
    license_on = models.ForeignKey(License,on_delete=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    rate = models.CharField(max_length=200)
    body = models.TextField(max_length=200)
    category = models.CharField(max_length=200,null=True)
    

class Comment(models.Model):
    author = models.CharField(max_length=200,null=True,default=1)
    student = models.ForeignKey(Student,on_delete=models.CASCADE, null=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
    