from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price_for_one = models.PositiveIntegerField()
    

    def __str__(self):
        return f'{self.id}, {self.name}, кол-во: {self.quantity}, цена: {self.price_for_one}$'