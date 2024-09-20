from django.db import models

# Create your models here.
class Item(models.Model):
    
    def __str__(self):
        return f"Item Name : " +self.item_name +" Item Description : "+ self.item_description +" Item Price : {self.item_price}"
    
    #ID field will be automatically generated
    item_name=models.CharField(max_length=200)
    item_description=models.CharField(max_length=200)
    item_price=models.IntegerField()
    item_image=models.CharField(max_length=500,default="https://tse3.mm.bing.net/th?id=OIP.htFK2Pzc1Xpg23Pwi_fezQHaE4&pid=Api&P=0&h=180")
    