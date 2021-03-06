# Generated by Django 4.0 on 2022-01-16 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0028_alter_menu_item_item_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu_item',
            name='components',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='menu_item',
            name='item_category',
            field=models.IntegerField(choices=[(0, 'Starter'), (2, 'Dessert'), (1, 'Main Course')]),
        ),
        migrations.AlterField(
            model_name='menu_item',
            name='menu_category',
            field=models.IntegerField(choices=[(1, 'Dinner'), (0, 'Lunch')]),
        ),
    ]
