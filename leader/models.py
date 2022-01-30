from django.db import models



class Leader(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50, null=True, blank=True)
    company = models.OneToOneField('company.Company', on_delete=models.CASCADE, primary_key=True)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'