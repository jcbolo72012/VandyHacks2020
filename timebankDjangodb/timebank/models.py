from django.db import models

# Create your models here.

class Member(models.Model):
    fname = models.CharField(max_length = 50)
    lname = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 200)
    passwd = models.CharField(max_length = 50)
    age = models.IntegerField()
    credits = models.IntegerField()
    cname = models.CharField(max_length = 100)
    def __str__(self):
        return self.fname + ' ' + self.lname
        
class TempMember(models.Model):
    fname = models.CharField(max_length = 50)
    lname = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 200)
    passwd = models.CharField(max_length = 50)


class Community(models.Model):
    cname = models.CharField(max_length = 100)
    members = models.IntegerField