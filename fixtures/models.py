from django.db import models

class Fixture(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    count = models.PositiveIntegerField()

    def __str__(self):
        return self.name