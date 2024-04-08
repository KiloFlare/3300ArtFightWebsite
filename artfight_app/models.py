from django.db import models
from django.urls import reverse

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])

class IndividualArt(models.Model):
    title = models.CharField(max_length=200)
    artPiece = models.ImageField()
    description = models.TextField(blank = True)
    user=models.ForeignKey(User, on_delete=models.RESTRICT)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('individualArt-detail', args=[str(self.id)])

