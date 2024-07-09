from django.db import models
from gic_cms.utils import generate_unique_hash

# Create your models here.

class Incubation(models.Model):
    start_up_title = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    founders_name = models.CharField(max_length=100)
    founders_email = models.EmailField()
    founders_contact = models.CharField(max_length=10)
    cofounders_name = models.CharField(max_length=100,null=True,blank=True)
    cofounders_email = models.EmailField(null=True,blank=True)
    cofounders_contact = models.CharField(max_length=10,null=True,blank=True)
    team_size = models.PositiveIntegerField()    
    domain = models.CharField(max_length=100)
    description = models.TextField()
    incubation_form_url = models.URLField()
    aadhar_url = models.URLField()
    slug = models.SlugField(unique=True,null=True,blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_hash()
        super(Incubation, self).save(*args, **kwargs) 
    
    def __str__(self):
        return self.start_up_title
    
class Inquiry(models.Model):
    email = models.EmailField()
    start_up_title = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)    
    incorporated = models.CharField(max_length=255)
    description = models.TextField()
    startup_stage =models.CharField(max_length=255)
    needed_support = models.CharField(max_length=255)
    incubated = models.TextField()
    team_size = models.PositiveIntegerField()    
    raised_fund_amount = models.PositiveIntegerField(null=True,blank=True)
    funding_agency = models.CharField(max_length=255,null=True,blank=True)
    pitch_deck_url = models.URLField(null=True,blank=True)
    slug = models.SlugField(unique=True,null=True,blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_hash()
        super(Inquiry, self).save(*args, **kwargs) 
    
    def __str__(self):
        return self.name
    
class ReachOut(models.Model):
    email = models.EmailField()    
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)
    message = models.TextField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_hash()
        super(ReachOut, self).save(*args, **kwargs) 
    
    def __str__(self):
        return self.name
    