from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField()
    tags = models.ManyToManyField('TagProject')
    def __str__(self):
        return self.title

class TagProject(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    def __str__(self):
        return self.name
