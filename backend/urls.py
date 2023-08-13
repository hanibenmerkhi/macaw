from django.urls import path 
from . import views

urlpatterns = [
    path('', views.produits ,name='produit') ,
    path('promotion', views.promotions ,name='pro') ,
    path('pack', views.packs ,name='pack') ,
    path('form/<int:id>', views.form ,name='form') ,
    path('detail/<int:id>', views.details ,name='details') ,
    path('achat', views.achat ,name='achat') ,
    
    

    ]