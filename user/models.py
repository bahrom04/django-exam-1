from django.db import models
from common.models import BaseModel


class User(BaseModel):
    username     = models.CharField(max_length=255)
    password     = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    birthday     = models.DateField()
    image        = models.ImageField(upload_to='static/user_images/')

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username
    




