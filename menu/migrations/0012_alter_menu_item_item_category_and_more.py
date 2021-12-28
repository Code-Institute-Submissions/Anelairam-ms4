# Generated by Django 4.0 on 2021-12-28 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0011_alter_menu_item_item_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu_item',
            name='item_category',
            field=models.IntegerField(choices=[(0, 'Dessert'), (0, 'Main Course'), (0, 'Starter')], default=0),
        ),
        migrations.AlterField(
            model_name='menu_item',
            name='menu_category',
            field=models.IntegerField(choices=[(1, 'Dinner'), (0, 'Lunch')], default=0),
        ),
    ]
