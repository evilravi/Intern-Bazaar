from django.contrib.auth.models import Permission, User
from django.db import models
import datetime

from django.core.urlresolvers import reverse



class Internship(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=200)
    company_logo= models.FileField(default='')
    Post = models.CharField(max_length=100)
    about = models.CharField(max_length=1500)
    role = models.CharField(max_length=1000)
    time = models.CharField(max_length= 10)
    benefits = models.CharField(max_length= 1500)
    skills = models.CharField(max_length = 1000)
    stud = models.CharField(max_length = 50000, null=True)

    def get_absolute_url(self):
        return reverse('intern:detail', kwargs={'pk' : self.pk})

    def __str__(self):
        return self.company_logo.url + '-' + self.Post


class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    intern = models.CharField(max_length=10000, null=True)
    user = models.CharField(max_length=250)
    email_id = models.CharField(max_length = 250)
    resume_file = models.FileField(default='')

    def __str__(self):
        return self.user


class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    date = models.DateTimeField()
    writer = models.CharField(max_length= 250)
    def __str__(self):
        return self.title