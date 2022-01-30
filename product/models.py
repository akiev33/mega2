from django.db import models


class Product(models.Model):
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price_for_one = models.PositiveIntegerField()
    

    def __str__(self):
        return f'{self.company} - {self.name}, цена: {self.price_for_one}с'