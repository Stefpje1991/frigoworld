from django.db import models

class ItemCategorie(models.Model):
    naam = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.naam

class Item(models.Model):
    naam = models.CharField(max_length=100)
    beschrijving = models.TextField(blank=True, null=True)
    prijs = models.DecimalField(max_digits=10, decimal_places=2)
    beschikbaar = models.BooleanField(default=True)
    categorie = models.ForeignKey(ItemCategorie, on_delete=models.SET_NULL, null=True, blank=True, related_name='items')
    inhoud = models.CharField(max_length=100, blank=True, null=True)
    foto = models.ImageField(upload_to='item_fotos/', blank=True, null=True)

    def __str__(self):
        return self.naam