# Generated by Django 4.0 on 2021-12-29 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0013_alter_menu_item_item_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu_item',
            name='item_category',
            field=models.IntegerField(choices=[(0, 'Main Course'), (0, 'Starter'), (0, 'Dessert')], default=0),
        ),
    ]
