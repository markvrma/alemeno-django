import uuid
from django.db import models
# each file uploaded will have a unique name


def update_filename(instance, filename):
    '''
    updates file name to ensure no file names repeat
    '''
    return f'uploads/{instance.id}_{filename}'

# Create your models here.
# file model


class StripFile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.ImageField(upload_to=update_filename)
    color_values = models.JSONField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
