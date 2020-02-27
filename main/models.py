from django.db import models
from django.contrib.auth.models import User


path = "static/data"


class ObjectClassModel(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class AnnotationClass(models.Model):
    image = models.FileField(upload_to=path)
    file_path = models.FileField(upload_to=path)
    name = models.ForeignKey(ObjectClassModel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
