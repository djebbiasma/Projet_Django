from django.db import models

# Create your models her
#class Product(models.Model):
   # name=models.CharField(max_length=100)
    #stock_count=models.IntegerField(default=0)
   # price=models.DecimalField(max_digits=6,decimal_places=2)


class Product(models.Model):
        name=models.CharField(max_length=100)
        stock_count=models.IntegerField(default=0)
        price=models.DecimalField(max_digits=6,decimal_places=2, default=0)
        description=models.TextField(default="",blank=True)
        sku=models.CharField ( verbose_name="Stock Keeping Unit", max_length=20, unique=True, null=True)



def __str__(self):
        return self.name

class ProductImage(models.Model):
        image=models.ImageField()
        product=models.ForeignKey('Product',on_delete=models.CASCADE,null=True)

class Categorie(models.Model):
        name=models.CharField(max_length=100)
        products=models.ManyToManyField('Product')