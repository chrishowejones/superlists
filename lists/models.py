from django.db import models


# Item class
class Item(models.Model):
    text = models.TextField(default='')
