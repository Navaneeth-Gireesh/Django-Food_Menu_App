from django.db import models

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=250)
    item_description = models.TextField()
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default='https://www.womantowomanmentoring.org/wp-content/uploads/placeholder.jpg')

    def __str__(self):
        return self.item_name