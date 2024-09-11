from django.db import models

# Create your models here.


class Dicty(models.Model):
    key = models.CharField(max_length=240, db_index=True)
    value = models.CharField(max_length=240, db_index=True)

    def __str__(self):
        return self.key
