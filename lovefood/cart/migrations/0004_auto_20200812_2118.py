# Generated by Django 2.2.13 on 2020-08-12 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20200812_2055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart_item',
            name='price',
        ),
        migrations.RemoveField(
            model_name='cart_item',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='order_items',
            name='price',
        ),
    ]
