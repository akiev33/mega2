from django.db import models



class Bank_account(models.Model):
    money = models.PositiveIntegerField()
    company = models.OneToOneField('company.Company', on_delete=models.CASCADE, primary_key=True)

    
    def __str__(self):
        return f'{self.money}$ -> {self.company_id}'
        