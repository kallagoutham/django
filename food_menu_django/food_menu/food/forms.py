from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    #consists the meta data for the Item form we have to kept ModelForm so that for that model we are creating a form
    class Meta:
        #for which model we are creating the form.  
        model=Item
        #fields for which form should be used
        fields=['item_name','item_description','item_price','item_image']