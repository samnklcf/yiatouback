from django.db import models
from django.contrib.auth.models import User, Group, Permission
import datetime
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    fullname= models.CharField(("Nom complet"), max_length=50)
    groups = models.ManyToManyField(Group, related_name='traduirepdf_groups')
    phone = models.IntegerField(verbose_name="Numéro de téléphone", default=000)
    birthdate_acheteurs = models.DateField(blank=True, null=True)
    GENRE_CHOICE = (
        ("HOMME", "HOMME"),
        ('FEMME', 'FEMME')
    )
    genre = models.CharField(("Genre"), max_length=50, choices=GENRE_CHOICE, default='HOMME')
    
    user_permissions = models.ManyToManyField(Permission, related_name='traduirepdf_user_permissions')
    
    home_address_acheteurs = models.CharField( verbose_name="Adresse",
        max_length=50, blank=True, null=True)
    condition = models.BooleanField(("Conditions"), default=False)
    class Meta:
        verbose_name = ("Donnés des utilisateurs")
        verbose_name_plural = ("Données des utilisateurs")

    def __str__(self):
        return self.email
    
    

    
    
class Categorie(models.Model):
    nom_categorie = models.CharField(max_length=255)

    class Meta:
        db_table = 'categorie'

    def __str__(self):
        return self.nom_categorie

class Requetes(models.Model):
    acheteur = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True)
    produit = models.CharField(max_length=255)
    image = models.ImageField(null=True)
    description = models.CharField(max_length=255)
    quantite = models.IntegerField()
    prix = models.IntegerField()
    satisfaite = models.BooleanField(default=False)
    nouveau_prix = models.IntegerField(blank=True, null=True)
    nombre_vues = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, auto_now=True, auto_now_add=False)

    class Meta:
        db_table = 'requetes'
        verbose_name = 'requete'

    def __str__(self):
        return self.produit


class Boutique(models.Model):
    proprio = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False)
    nom = models.CharField(("Nom de la boutique"), max_length=50, default="Aucun nom")
    phone = models.IntegerField(verbose_name="Téléphone de la boutique", default=000)
    office_adresse = models.CharField(("Lieu de vente"),max_length=50, blank=True, null=True, default="Mindoubé 1")
    categorie = models.ManyToManyField(Categorie, blank=True, default=[1])
    requetes = models.ManyToManyField(Requetes, blank=True, default=[1])
    Date = models.DateField(("Date de création"), auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = ("BOUTIQUE")
        verbose_name_plural = ("BOUTIQUES")

    def __str__(self):
        return self.nom

    




    