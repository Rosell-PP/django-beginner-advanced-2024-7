from django import forms
from django.core import validators
from ..models import Post

def start_ro(value):
    if value[:2] != 'Ro' and value[:2] != 'ro':
        raise forms.ValidationError("Debe iniciar con 'Ro'")

# Clase que representa un formulario para registrar un post
# class PostForm(forms.Form):
class PostForm(forms.ModelForm):
    ## for custom validation fields must override fields here
    post_title = forms.CharField(
        label="Titulo del post",
        label_suffix="",
        min_length=10,
        error_messages={
            'min_length':"El titulo debe contener mas de 10 caracteres"
        },
        help_text="Debe introducir un titulo para el post que no sea muy extenso",
        widget=forms.TextInput(attrs={
            'placeholder':"Titulo para el post",
            'class':'form-control'
        }),
        validators=[
            validators.MaxLengthValidator(
                limit_value=100,
                message="No debe contener mas de 100 carecteres !!"
            ),
            start_ro
        ]
    )

    class Meta:
        model = Post
        
        # fields = '__all__'        For all fiedls in model
        fields = [
            'post_title',
            'post_content',
            'post_image',
        ]

        # for exclude some fields in the form
        exclude = ['']  

        labels = {
            'post_title':'Titulo del post',
            'post_content':'Contenido',
            'post_image':'Imagen para el POST',
        }

        help_texts = {
            'post_title':'Debe introducir un titulo para el post que no sea muy extenso',
            'post_content':'Introduzca el contenido, puede ser extenso',
            'post_image':'Seleccione una imagen que represente al POST',
        }

        error_messages = {
            'post_title': {
                'min_length':"El titulo debe contener mas de 10 caracteres"
            }
        }

        widgets = {
            'post_title': forms.TextInput(attrs={
                'placeholder':"Titulo para el post",
                'class':'form-control'
            }),
            'post_content': forms.Textarea(attrs={
                'placeholder':"Conenido para el post",
                'class':'form-control',
                'rows':"5"
            }),
        }

    # title = forms.CharField(
    #     label="Titulo del post",
    #     label_suffix="",
    #     min_length=10,
    #     error_messages={
    #         'min_length':"El titulo debe contener mas de 10 caracteres"
    #     },
    #     help_text="Debe introducir un titulo para el post que no sea muy extenso",
    #     widget=forms.TextInput(attrs={
    #         'placeholder':"Titulo para el post",
    #         'class':'form-control'
    #     }),
    #     validators=[
    #         validators.MaxLengthValidator(
    #             limit_value=100,
    #             message="No debe contener mas de 100 carecteres !!"
    #         ),
    #         start_ro
    #     ]
    # );

    # content = forms.CharField(
    #     label="Contenido",
    #     label_suffix="",
    #     help_text="Introduzca el contenido, puede ser extenso",
    #     widget=forms.Textarea(attrs={
    #         'placeholder':"Conenido para el post",
    #         'class':'form-control',
    #         'rows':"5"
    #     })
    # );

    # Personalizacion de la validacion del formulario completo
    # same for form class and formModel class
    # def clean(self):
    #     cleaned_data = super().clean()

    #     title = cleaned_data["title"]
    #     content = cleaned_data["content"]

    #     if title[0] != 'r' and title[0] != 'R':
    #         raise forms.ValidationError("El titulo debe comenzar con la letra R o r")





