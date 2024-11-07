from django.db import models

# Create your models here.
class Tag(models.Model):
    # Attributes or database table fields

    # Nombre de la Etiqueta
    name = models.CharField(
        max_length=50,
        db_comment="Nombre de la Etiqueta"
    );

    def __str__(self):
        return f"{self.name}"
