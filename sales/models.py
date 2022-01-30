
from tkinter import CASCADE
from django.db import models


class Sale(models.Model):
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    sales_product = models.PositiveIntegerField()
    date_time = models.DateTimeField()


    def __str__(self):
        return f'{self.product}, Кол-во проданных:{self.sales_product}'