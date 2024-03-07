from django.db import models
from django.urls import reverse

# Create your models here.
class register_table(models.Model):
    name1=models.CharField(max_length=20)
    email1=models.EmailField()
    password1=models.CharField(max_length=20)

class brand(models.Model):
    name= models.CharField(max_length=250,unique = True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'brands'
        verbose_name_plural = 'brands'
    def __str__(self):
        return '{}'.format(self.name)

class product_tbl(models.Model):
    SIZE_CHOICES = [
        ('5', '5'),
        ('6', '6'),
        # ('7', '7'),
        # ('8', '8'),
        # ('9', '9'),
        # ('10', '10'),
        # ('11', '11'),
        # ('12', '12'),
    ]
    product_name= models.CharField(max_length=40)
    brand= models.CharField(max_length=20,null=True)
    product_image=models.FileField(upload_to='pictures')
    product_price=models.IntegerField()
    product_des=models.TextField(null=True)
    stock=models.IntegerField(null=True)
    size = models.CharField(max_length=5, choices=SIZE_CHOICES, null=True)


    def __str__(self):
        return self.product_name
  
