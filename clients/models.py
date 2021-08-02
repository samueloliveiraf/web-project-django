from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=9)


    def __str__(self):
        return self.first_name


    class Meta:
        db_table = 'clientes'
