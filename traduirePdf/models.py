from django.db import models
from django.contrib.auth.models import User, Group, Permission
import datetime
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    groups = models.ManyToManyField(Group, related_name='traduirepdf_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='traduirepdf_user_permissions')
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


class Shops(models.Model):
    fullname_shops = models.CharField(max_length=50)
    nombre_employes = models.IntegerField()
    detailed_location = models.TextField()
    phone_shops = models.IntegerField()
    office_address_acheteurs = models.CharField(
        max_length=50, blank=True, null=True)
    home_address_acheteurs = models.CharField(
        max_length=50, blank=True, null=True)
    categorie = models.ManyToManyField(Categorie)

    class Meta:
        db_table = 'shops'
        verbose_name = 'shop'

    def __str__(self):
        return self.fullname_shops





class Acheteurs(models.Model):
    fullname_acheteurs = models.OneToOneField(User, on_delete=models.CASCADE)
    email_acheteurs = models.EmailField(max_length=100, unique=True)
    birthdate_acheteurs = models.DateField(blank=True, null=True)
    phone_acheteurs = models.IntegerField()
    office_address_acheteurs = models.CharField(
        max_length=50, blank=True, null=True)
    home_address_acheteurs = models.CharField(
        max_length=50, blank=True, null=True)
    categorie = models.ManyToManyField(Categorie)

    class Meta:
        db_table = 'acheteurs'
        verbose_name = ("Acheteur")

    def __str__(self):
        return self.fullname_acheteurs


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
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'requetes'
        verbose_name = 'requete'

    def __str__(self):
        return self.produit


class Vendeurs(models.Model):

    fullname = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=100)
    birthdate = models.DateField(blank=True, null=True)
    phone = models.IntegerField()
    office_adress = models.CharField(max_length=50, blank=True, null=True)
    home_adress = models.CharField(max_length=50, blank=True, null=True)
    shop = models.ManyToManyField(Shops)
    categorie = models.ManyToManyField(Categorie)
    requetes = models.ManyToManyField(Requetes)

    class Meta:
        db_table = 'vendeurs'
        verbose_name = 'vendeur'

    def __str__(self):
        return self.fullname

    




    