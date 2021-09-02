from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    quantity = models.IntegerField(default=0)
    details = models.CharField(max_length=250, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('home')

    def p_total(self):
        total = self.price * self.quantity
        return total

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'produtos'


class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False,null=False)
    time = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField()

    def __str__(self):
	    return '{} {} {}'.format(self.product.quantity, self.product.title, self.time)
