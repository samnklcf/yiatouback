from django.db import models

# Create your models here.


class Liste(models.Model):
    nom = models.CharField(("Nom"), max_length=50, null=True, blank=True)
    Prix = models.CharField(("Prix"), max_length=50, null=True, blank=True)
    fichier = models.FileField(("fichier"), upload_to="fichier/pdf", max_length=100, null=True)
    

    class Meta:
        verbose_name = ("Liste")
        verbose_name_plural = ("Listes")

    def __str__(self):
        return self.nom

class CleApi(models.Model):
    nom = models.CharField(("Nom"), max_length=400, null=False, blank=True)
    cle = models.CharField(("clé de l'Api"), max_length=400, null=False, blank=True)
    
    class Meta:
        verbose_name = ("Clé Api")
        verbose_name_plural = ("Clés Api")

    def __str__(self):
        return self.nom
    