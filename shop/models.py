from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=100, default="")
    price = models.IntegerField(default=0)
    product_desc = models.CharField(max_length=1000)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    con_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    email=models.EmailField(default="")
    mobileno=models.IntegerField(default=0)
    feedback=models.CharField(max_length=1000,default="")

    def __str__(self):
        return self.name

class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    itemjson=models.CharField(max_length=5000)
    fname=models.CharField(max_length=25)
    lname=models.CharField(max_length=25,default="")
    email=models.EmailField(max_length=50,default="")
    address1=models.CharField(max_length=50,default="")
    address2=models.CharField(max_length=50,default="")
    mobileno=models.IntegerField(default=0)
    state=models.CharField(max_length=10,default=0)
    zipcode=models.IntegerField(default=0)
    total=models.IntegerField(default=0)

    def __str__(self):
        return self.fname

