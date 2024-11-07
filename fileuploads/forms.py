from django import forms
from .models import UserData

class FileUploadForm(forms.ModelForm):


    class Meta:
        model =  UserData
        
        fields = '__all__'

        
        