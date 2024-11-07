from django.db import models
from django.contrib.auth.models import User;
from .tag_model import Tag

# Create your models here.
class Post(models.Model):
    # Attributes or database table fields

    # Titulo del post
    post_title = models.CharField(
        max_length=100,
        db_comment="Titulo del post"
    );

    # Contenido del post
    post_content = models.TextField(
        db_comment= "Contenido del post"
    );

    # Imagen en el post
    post_image = models.ImageField(
        upload_to="posts/",
        null=True
    )

    # Fecha de publicado el post
    published_date = models.DateTimeField(
        auto_now=True,
        db_comment = "Fecha de publicado el post"
    );

    # Etiquetas relacionadas
    tags = models.ManyToManyField(to=Tag)

    def __str__(self):
        return f"{self.post_title}"
