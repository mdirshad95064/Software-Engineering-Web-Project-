from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 300)
    slug = models.CharField(max_length = 500,blank = True) #use unique = True in slug in real project
    icon = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length = 300)
    slug = models.CharField(max_length = 500,blank = True)
    category = models.ForeignKey(Category,on_delete = models.CASCADE)

    def __str__(self):
        return self.name

class Slider(models.Model):
    name = models.CharField(max_length = 300)
    image = models.ImageField(upload_to = 'media')
    description = models.TextField(blank = True)
    url = models.URLField(max_length = 500)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length = 300)
    image = models.ImageField(upload_to = 'media')
    slug = models.CharField(max_length = 500,blank = True)

    def __str__(self):
        return self.name

class Ad(models.Model):
    name = models.CharField(max_length = 300)
    image = models.ImageField(upload_to = 'media')
    description = models.TextField(blank = True)
    rank = models.IntegerField(default = 1)

    def __str__(self):
        return self.name

class Review(models.Model):
    name = models.CharField(max_length = 300)
    position = models.CharField(max_length = 200)
    image = models.ImageField(upload_to = 'media')
    description = models.TextField(blank = True)

    def __str__(self):
        return self.name

STOCK = (('in','In Stock'),('out', 'Out of Stock'))
LABELS = (('new','new'),('hot','hot'),('sale','sale'),('','default'))
class Product(models.Model):
    name = models.CharField(max_length = 300)
    slug = models.CharField(max_length = 500,blank = True)
    price = models.IntegerField()
    discounted_price = models.IntegerField()
    image = models.ImageField(upload_to = 'media')
    description = models.TextField(blank = True)
    specification = models.TextField(blank = True)
    category = models.ForeignKey(Category,on_delete = models.CASCADE)
    Subcategory = models.ForeignKey(SubCategory,on_delete = models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete = models.CASCADE)
    stock = models.CharField(choices = STOCK,max_length = 100)
    labels = models.CharField(choices = LABELS,blank = True,max_length = 100)

    def __str__(self):
        return self.name

