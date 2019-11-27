from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    Title = models.CharField(max_length=120)
    Description = models.TextField()
    Price = models.DecimalField(decimal_places=2,max_digits=20,null=True)
    Image = models.ImageField(upload_to='products/',null=True,blank=True)

    # def get_absolute_url(self):
    #     return "/products/pk/"

    def __str__(self):
        return self.Title