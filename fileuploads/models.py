from django.db import models

# Create your models here.
class UserData(models.Model):
    username = models.CharField(
        max_length=255
    )

    file = models.FileField(
        upload_to="userdata",
        blank=True,
        null=True
    )

    image = models.ImageField(
        upload_to="images",
        null=True,
        blank=True
    )