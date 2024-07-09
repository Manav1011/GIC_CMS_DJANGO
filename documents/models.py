from django.db import models
from gic_cms.utils import generate_unique_hash
from django.core.validators import FileExtensionValidator

# Create your models here.

class Report(models.Model):
    title = models.CharField(max_length=255)
    about = models.TextField()
    attachment = models.FileField(validators=[FileExtensionValidator(['pdf'])],upload_to="reports/")
    date = models.DateField()
    slug = models.SlugField(unique=True,null=True,blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_hash()
        super(Report, self).save(*args, **kwargs) 
    
    def __str__(self):
        return self.title

class Circular(models.Model):
    title = models.CharField(max_length=255)
    about = models.TextField()
    attachment = models.FileField(validators=[FileExtensionValidator(['pdf'])],upload_to="circulars/")
    date = models.DateField()
    slug = models.SlugField(unique=True,null=True,blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_hash()
        super(Circular, self).save(*args, **kwargs) 
    
    def __str__(self):
        return self.title