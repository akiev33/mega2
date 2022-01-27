from django.db import models



class Addres(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    apartment = models.CharField(max_length=100, null=True, blank=True)
    home = models.CharField(max_length=100, null=True, blank=True)
    mail_index = models.PositiveIntegerField()
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.company_id}, {self.country} -> {self.city} -> {self.street}'