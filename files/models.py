from django.db import models

# Create your models here.
class File(models.Model):
    File_name= models.CharField(max_length=100)
    upload = models.FileField(upload_to='uploads/')
    file_type= models.CharField( max_length = 20) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pk)