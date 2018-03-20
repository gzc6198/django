from django.db import models

# Create your models here.


class Text(models.Model):
    name = models.CharField(max_length=255)
    class Meta():
        db_table = 'text'

    @classmethod
    def create(cls,t):
        obj = cls(name = t)
        return obj

