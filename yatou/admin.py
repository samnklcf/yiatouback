from django.contrib import admin
from .models import *



    
class CategorieAdmin(admin.ModelAdmin):
    list_display = ['nom_categorie', ]
    
        
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', "id", "genre" ]



class VendeursAdmin(admin.ModelAdmin):
    list_display = ['phone',
                    'office_adress',
                    "Date"
                    ]


class requetesAdmin(admin.ModelAdmin):
    list_display = ['produit',
                    'description', 'quantite', 'prix', 'satisfaite',
                    'nouveau_prix', 'nombre_vues', 'created_at'
                    ]
    list_filter = ['produit', 'satisfaite', 'nombre_vues', 'created_at']


class BoutiqueAdmin(admin.ModelAdmin):
    list_display = ["nom", "office_adresse", "Date"
                    ]


admin.site.register(Requetes, requetesAdmin)
admin.site.register(Boutique, BoutiqueAdmin)
admin.site.register(Categorie, CategorieAdmin)



admin.site.register(User, UserAdmin)


# Register your models here.
