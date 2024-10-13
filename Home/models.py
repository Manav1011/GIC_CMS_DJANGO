from django.db import models
from gic_cms.utils import generate_unique_hash
from django.core.validators import FileExtensionValidator

class Stats(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,null=True,blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_hash()
        super(Stats, self).save(*args, **kwargs) 

    def __str__(self):
        return self.title
    
class Partner(models.Model):
    logo = models.FileField(validators=[FileExtensionValidator(['webp','png','jpg'])],upload_to="partner-logos/")
    title = models.CharField(max_length=255)
    about = models.TextField()
    slug = models.SlugField(unique=True,null=True,blank=True)

    def save(self, *args, **kwargs):
        print(self.logo.chunks)
        if not self.slug:
            self.slug = generate_unique_hash()
        super(Partner, self).save(*args, **kwargs) 
    
    def __str__(self):
        return self.title

class Quote(models.Model):
    author = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField(unique=True,null=True,blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_hash()
        super(Quote, self).save(*args, **kwargs) 
    
    def __str__(self):
        return self.author

class ImageGallery(models.Model):
    title = models.CharField(max_length=255)
    image = models.FileField(validators=[FileExtensionValidator(['webp','png','jpg'])],upload_to="image-gallery/")
    slug = models.SlugField(unique=True,null=True,blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_hash()
        super(ImageGallery, self).save(*args, **kwargs) 

    def __str__(self):
        return self.titled