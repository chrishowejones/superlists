from django.db import models


# List class
class List(models.Model):
    pass


# Item class
class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)
