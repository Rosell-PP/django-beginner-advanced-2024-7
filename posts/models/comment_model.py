from django.db import models
from .post_model import Post

# Create your models here.
class Comment(models.Model):
    # Attributes or database table fields

    # Titulo del post
    comment = models.TextField(
        db_comment="El comentario de un usuario"
    );

    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.comment}"
