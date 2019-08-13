from django import forms
from .models import Upload

class UploadForm(forms.ModelForm):
    
    
    class Meta:
        model = Upload
        fields = ['title','description','upload_file','send_to']