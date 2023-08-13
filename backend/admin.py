from django.contrib import admin

# Register your models here.
from .models import produit,demande
admin.site.register(produit)
admin.site.register(demande)
