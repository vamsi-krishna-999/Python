from django.db import models


class BookModels(models.Model):
    name = models.CharField(max_length=99)
    auth = models.CharField(max_length=59)
    read_by = models.CharField(max_length=59)


