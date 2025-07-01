from django.db import models

# Create your models here.
class Singer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    genre = models.CharField(max_length=20)
    content = models.CharField(max_length=50)
    debut = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Song(models.Model):
    id = models.AutoField(primary_key=True)
    singer = models.ForeignKey(Singer,blank=False,null=False,on_delete=models.CASCADE,related_name='songs')
    title = models.CharField(max_length=50)
    release = models.DateField()
    content = models.CharField(max_length=50)