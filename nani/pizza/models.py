from django.db import models

# Create your models here.

class Size(models.Model):
    title = models.CharField(max_length=40)

    def __str__ (self):
        return self.title

class Pizza(models.Model):
    topping1 = models.CharField(max_length=50)
    topping2 = models.CharField(max_length=50)
    topping3 = models.CharField(max_length=50)
    topping4 = models.CharField(max_length=50)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
