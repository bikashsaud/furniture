from django.db import models

# Create your models here.
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Furniture(models.Model):
    furniture_code = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.furniture_code

