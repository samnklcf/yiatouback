# Generated by Django 4.2.1 on 2023-06-08 15:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yatou', '0006_boutique_delete_responsable'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='boutique',
            options={'verbose_name': 'BOUTIQUE', 'verbose_name_plural': 'BOUTIQUES'},
        ),
        migrations.AlterField(
            model_name='vendeurs',
            name='proprio',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Propritaire'),
        ),
    ]