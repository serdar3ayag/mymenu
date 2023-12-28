from django.db import models

# Create your models here.

class Category(models.Model):
    name_ru = models.CharField(max_length = 50, null=True)
    name_en = models.CharField(max_length = 50, null=True)
    image = models.ImageField(upload_to='media/', null=True)

    def __str__(self):
        return self.name_ru

    
class Dish(models.Model):
    name_ru = models.CharField(max_length = 50, null=True)
    name_en = models.CharField(max_length = 50, null=True)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()

    def __str__(self):
        return self.name_ru
