from django import forms
from django.core import validators
from ..models import Comment


# Clase que representa un formulario para registrar un comentario sobre un post
class CommentForm(forms.ModelForm):
    ## for custom validation fields must override fields here

    

    class Meta:
        model = Comment
        
        fields = '__all__'

        # fields = [
        # ]

        # for exclude some fields in the form
        # Excluimos el post porque vamos a comentar desde los detalles de uno
        exclude = ['post']  

        labels = {
        }

        help_texts = {
        }

        error_messages = {
            
        }

        widgets = {
            'comment': forms.Textarea(attrs={
                'placeholder':"Su comentario sobre el post",
                'class':'',
                'rows':"3"
            }),
        }

    