# used to links/ define url patterns in general
from . import views
from django.urls import path

#Namespacing
app_name = 'food'
urlpatterns = [
    path('',views.index,name='index'),
    path('items/',views.items,name='items'),
    #@pathvariable in spring boot.
    path('<int:item_id>/',views.detail,name="details"),
    #add items
    path('add/',views.createItem,name="addItem"),
    #Update the items
    path('update/<int:item_id>',views.updateItem,name="updateItem"),
    #Delete the item
    path('delete/<int:item_id>',views.deleteItem,name='deleteItem')
]