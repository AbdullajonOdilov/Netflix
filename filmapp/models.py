from django.contrib.auth.models import User
from django.db import models
from rest_framework.viewsets import ModelViewSet


class Actor(models.Model):
    ism = models.CharField(max_length=20)
    jins = models.CharField(max_length=6)
    davlat = models.CharField(max_length=20)
    t_yil = models.DateField()
    def __str__(self):return self.ism

class Kino(models.Model):
    nom = models.CharField(max_length=20)
    janr = models.CharField(max_length=20,blank=True)
    yil = models.DateField()
    reyting = models.FloatField()
    actors = models.ManyToManyField(Actor)
    def __str__(self):return self.nom
class Comment(models.Model):
    matn = models.TextField()
    sana = models.DateField()
    kino = models.ForeignKey(Kino,on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

