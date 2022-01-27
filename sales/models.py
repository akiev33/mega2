
from django.db import models



class Sale(models.Model):
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE)
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    sales_product = models.PositiveIntegerField()
    date_time = models.DateTimeField()


    def __str__(self):
        return f'{self.company_id} - {self.product_id}, Кол-во проданных:{self.sales_product}'