
from django.db import models

# Create your models here.
class Audio_store(models.Model):
    Audio_file = models.FileField(upload_to='docs/')
    class Meta:
        db_table = 'Audio_store'
