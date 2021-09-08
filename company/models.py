from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Company(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='company/', blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('home')


    def __str__(self):
        return self.name


    class Meta:
        db_table = 'empresa'

