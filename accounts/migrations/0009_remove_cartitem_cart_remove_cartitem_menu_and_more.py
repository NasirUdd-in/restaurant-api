# Generated by Django 4.2.9 on 2024-01-27 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_cart_order_orderitem_order_menu_order_user_cartitem_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='menu',
        ),
        migrations.RemoveField(
            model_name='order',
            name='menu',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='menu',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
