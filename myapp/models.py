#from django.contrib.auth.models import User

from django.db import models




#import uuid

class ProductDetails(models.Model):
    name = models.CharField(max_length=255)
    CATEGORY=[
        ('chairs','Chairs'),
        ('sofas', 'Sofas'),
        ('dining&kitchen', 'Dining&Kitchen'),
        ('study&office', 'Study&Office'),
        ('wardrobes', 'Wardrobes'),
        ('lamp&lighting', 'Lamp&Lighting'),
        ('bedroom', 'BedRoom')
    ]
    category=models.CharField(max_length=20, choices=CATEGORY)
    description = models.TextField()
    price = models.CharField(max_length=20)
    picture = models.ImageField(upload_to='static/productimages/', null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def _str_(self):
        return self.name + ' - ' + self.email

'''
class Cart(models.Model):
    id = models.UUIDField(default=uuid.uuid4,primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed= models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

class CartItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='items')
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name="cartitems")
    quantity=models.IntegerField(default=0)

    def __str__(self):
        return self.product.name
'''


