import uuid
from django.db import models

# Create your models here.
# file model


class StripFile(models.Model):
    image = models.ImageField(upload_to='uploads/')
    color_values = models.JSONField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    
