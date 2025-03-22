from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    kind = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    expire_year = models.IntegerField(
        validators=[
            MinValueValidator(2026), 
            MaxValueValidator(2026),  
        ]
    )

    def __str__(self):
        return self.kind
