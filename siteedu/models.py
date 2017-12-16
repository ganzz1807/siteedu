from django.db import models
from django.utils import timezone
from django.core.files.base import File
from django.core.files.images import ImageFile

class Post(models.Model):
   title = models.CharField(max_length=500)
   created_date = models.DateTimeField    
   image = models.ImageField  (upload_to='website_image')
   education_logo = models.CharField(max_length=1000)
 
   def get_absolute_url(self):
       self.created_date = timezone.now()
       self.save() 
   def __str__(self):
       return self.title
   def __str__(self):
       return self.education_logo
       



  
