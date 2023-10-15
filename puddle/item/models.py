from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',) # , after name because it's iterable
        verbose_name_plural = 'Categories'

    def __str__(self): #shows the names for Categories
        return self.name

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE) #if Category is deleted, all items from Category are also deleted
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items',on_delete=models.CASCADE) #if user is deleted, all items by them will be deleted
    created_at = models.DateField(auto_now_add=True)

    def __str__(self): #shows the names for Categories
        return self.name
