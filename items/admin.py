from django.contrib import admin
from .models import Item, ItemCategorie

@admin.register(ItemCategorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('naam',)
    search_fields = ('naam',)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('naam', 'prijs', 'beschikbaar', 'categorie', 'inhoud')
    search_fields = ('naam', 'beschrijving')
    list_filter = ('beschikbaar', 'categorie')