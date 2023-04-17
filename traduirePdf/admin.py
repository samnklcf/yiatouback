from django.contrib import admin
from .models import *



    
class CategorieAdmin(admin.ModelAdmin):
    list_display = ['nom_categorie', ]


class AcheteursAdmin(admin.ModelAdmin):
    list_display = ['fullname_acheteurs', 'email_acheteurs',
                    'phone_acheteurs']


class VendeursAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'email', 'birthdate', 'phone',
                    'home_adress']


class requetesAdmin(admin.ModelAdmin):
    list_display = ['produit',
                    'description', 'quantite', 'prix', 'satisfaite',
                    'nouveau_prix', 'nombre_vues', 'created_at'
                    ]
    list_filter = ['produit', 'satisfaite', 'nombre_vues', 'created_at']


class ShopsAdmin(admin.ModelAdmin):
    list_display = ['fullname_shops', 'nombre_employes', 'detailed_location',
                    'phone_shops', 'office_address_acheteurs', 'home_address_acheteurs'
                    ]


admin.site.register(Requetes, requetesAdmin)
admin.site.register(Shops, ShopsAdmin)
admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Acheteurs, AcheteursAdmin)
admin.site.register(Vendeurs, VendeursAdmin)


admin.site.register(User)


# Register your models here.
