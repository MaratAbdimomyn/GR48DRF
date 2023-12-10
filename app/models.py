from django.db import models

class Cars(models.Model):
    brand = models.CharField(max_length=40)
    model = models.CharField(max_length=40)
    engine = models.CharField(max_length=40)
    power = models.CharField(max_length=40)

    def __str__(self):
        return self.name