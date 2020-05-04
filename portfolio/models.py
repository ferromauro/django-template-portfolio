from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField()
    description = models.TextField()
    image = models.ImageField()
    tags = models.ManyToManyField('TagProject')

class TagProject(models.Model):
    name = models.CharField()
    description = models.CharField()