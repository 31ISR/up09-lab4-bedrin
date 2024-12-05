from django.db import models

class Community(models.Model):
       name = models.CharField(max_length=75)
       description = models.CharField(max_length=150)
       slug = models.SlugField(unique=True)
       date = models.DateTimeField(auto_now_add=True, null=True)
       free = models.BooleanField(default=False)

       def __str__(self):
           return self.name
   
