# Generated by Django 4.2.3 on 2023-07-28 02:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Demand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('product_name', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=200)),
                ('price', models.CharField(blank=True, max_length=200, null=True)),
                ('new_price', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='demand/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_demands', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Demand',
                'indexes': [models.Index(fields=['product_name', 'slug'], name='demand_dema_product_df24f7_idx'), models.Index(fields=['price', 'new_price'], name='demand_dema_price_d68f98_idx'), models.Index(fields=['description'], name='demand_dema_descrip_8eecc8_idx')],
            },
        ),
    ]