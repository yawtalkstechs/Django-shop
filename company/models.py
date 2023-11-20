# company/models.py
from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    registration_date = models.DateField(auto_now_add=True)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    logo_url = models.URLField()

    class Meta:
        verbose_name = "company"
        verbose_name_plural = "companies"

    def __str__(self):
        return self.name
