from django.db import models

class Bin(models.Model):
    bin_id = models.CharField(max_length=10, unique=True)
    location = models.CharField(max_length=255)
    weight = models.FloatField(default=0.0)  # Weight in kilograms
    trash_level = models.IntegerField(default=0)  # Trash level as a percentage
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Bin {self.bin_id} - {self.trash_level}% full"
