# Generated by Django 4.2.9 on 2024-01-27 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_restaurant_items_restaurant_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Item', to='accounts.user'),
        ),
        migrations.AddField(
            model_name='menu',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Menu', to='accounts.user'),
        ),
    ]