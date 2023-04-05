from django.db import models

# Create your models here.

class Archivo(models.Model):
    csv = models.FileField(upload_to="csvtohtmlapp/")
