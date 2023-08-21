# Generated by Django 4.2.3 on 2023-08-21 13:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('demand', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demand',
            name='status',
            field=models.CharField(blank=True, choices=[('pending', 'Pending'), ('reschedule', 'Reschedule'), ('validate', 'Validate'), ('confirm', 'Confirm'), ('cancel', 'Cancel'), ('refuse', 'Refuse'), ('archive', 'Archive'), ('new_proposal', 'New Proposal'), ('past', 'Past')], default='pending', max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('demand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='demand_messages', to='demand.demand')),
                ('receiver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiver_user_messages', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sender_user_messages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]