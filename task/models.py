from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.conf import Settings
from datetime import datetime

# Create your models here.

class Upload(models.Model):
    uploaded_by = models.CharField(max_length = 20)
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=150)
    upload_file = models.FileField(upload_to='files%y%m%d')
    send_to = models.EmailField(max_length=70, null= False)

    def __str__(self):
        title = self.title
        return title


    

    
# qs = User.objects.filter(groups__name__in=['Recipient'])
# contacts = [
#     str(username) for username in qs
# ]
