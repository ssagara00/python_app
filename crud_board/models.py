from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField("氏名", max_length=255)
    email = models.CharField("E-Mail", max_length=255)
    age = models.IntegerField("年齢", blank=True)

    def __str__(self):
        return self.name
