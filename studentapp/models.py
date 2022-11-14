from django.db import models
# from django.core.exceptions import ValidationError
from studentapp.validators import age_validation


# Create your models here.

choice=[('---','---'),('+1','+1'),('+2','+2')]

class Student(models.Model):
    Full_Name=models.CharField(max_length=50,blank=False,null=True)
    Email = models.EmailField(max_length=100,blank=False,null=True)
    Age = models.IntegerField(validators=[age_validation])
    Class =models.CharField(max_length=40,choices = choice,default='---')
    Description= models.TextField(max_length=400,null=True,blank=True)  

    def __str__(self):
        return self.Full_Name

   