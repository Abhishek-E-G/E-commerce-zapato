from django.db import models
from Zapatoapp.models import product_tbl
# Create your models here.
 
# cart creattion
class Cart(models.Model):
    cart_id = models.CharField(max_length=250,blank=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Cart'
        ordering = ['date_added']

    def __str__(self):
        return '{}'.format(self.cart_id)


#  cart and count, quantity,price
class CartItem(models.Model):
    product = models.ForeignKey(product_tbl,on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)

    quantity = models.IntegerField()
    active = models.BooleanField(default=True)
    total = models.IntegerField(null=True)
    selected_size = models.CharField(max_length=5, null=True) 
    class Meta:
        db_table = 'CartItem'

    def sub_total(self):
        return self.product.product_price * self.quantity
    
    def __str__(self):
        return '{}'.format(self.product)
  





# --------- direct buy ---------------
class Buy(models.Model):
    b_id = models.CharField(max_length=255,blank=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Buy'
        ordering = ['date_added']

    def __str__(self):
        return '{}'.format(self.b_id)
     
class Direct_buy(models.Model):
    # SIZE_CHOICES = [
    #     ('5', '5'),
    #     ('6', '6'),
    #     ('7', '7'),
    #     ('8', '8'),
    #     ('9', '9'),
    #     ('10', '10'),
    #     ('11', '11'),
    #     ('12', '12'),
    # ]
    product = models.ForeignKey(product_tbl,on_delete=models.CASCADE)
    b = models.ForeignKey(Buy,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)
    total = models.IntegerField(null=True)
    size = models.CharField(max_length=50, null=True,blank=True) 

    class Meta:
        db_table = 'Direct_buy'

    def sub_total(self):
        return self.product.product_price * self.quantity
    
    def __str__(self):
        return '{}'.format(self.product)