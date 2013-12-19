from django.db import models

class Pokemon(models.Model):
    id_pokemon = models.IntegerField()
    name = models.CharField(max_length=200)