from django.db import models

# Create your models here.

class Business(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    employee_size = models.IntegerField(default=0)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    owner_name = models.CharField(max_length=255)
    owner_phone_number = models.CharField(max_length=20)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

# name, description, employee_size, address, phone_number, owner_name, owner_phone_number, website
