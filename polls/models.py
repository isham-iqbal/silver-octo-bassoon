from django.db import models


class Bar(models.Model):
    value = models.CharField(max_length=256)
