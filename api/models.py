from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50, null=False, primary_key= True)
    email = models.EmailField(null=False, unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    profile_image = models.ImageField(upload_to='students/',blank=True, null=True)


    def __str__(self):
        return self.name