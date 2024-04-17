from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

#Permissions Stuffs
class Module(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Permission(models.Model):
    name = models.CharField(max_length=50)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=50)
    permissions = models.ManyToManyField(Permission)

    def __str__(self):
        return self.name

class UserRole(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.role.name

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])

class IndividualArt(models.Model):
    title = models.CharField(max_length=200)
    artPiece = models.ImageField(upload_to ='static/uploads/', blank=False, null=False)
    description = models.TextField(blank = True)
    user=models.ForeignKey(User, on_delete=models.RESTRICT)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('individualArt-detail', args=[str(self.id)])

