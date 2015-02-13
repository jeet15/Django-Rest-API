from django.db import models

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length = 30)
    game = models.CharField(max_length = 30)
    address = models.CharField(max_length = 60)
    is_active = models.NullBooleanField()

    class Meta:
            ordering = ('name',)