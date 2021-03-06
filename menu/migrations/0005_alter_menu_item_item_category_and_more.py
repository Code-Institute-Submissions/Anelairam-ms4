# Generated by Django 4.0 on 2021-12-27 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_menu_item_item_category_menu_item_menu_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu_item',
            name='item_category',
            field=models.IntegerField(choices=[(0, 'Starter'), (0, 'Dessert'), (0, 'Main Course')], default=0),
        ),
        migrations.AlterField(
            model_name='menu_item',
            name='menu_category',
            field=models.IntegerField(choices=[(0, 'Lunch'), (1, 'Dinner')], default=0),
        ),
    ]
