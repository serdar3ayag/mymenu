# Generated by Django 4.2.3 on 2023-12-24 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0005_alter_dish_options_dish_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dish',
            options={},
        ),
        migrations.RemoveField(
            model_name='dish',
            name='order',
        ),
    ]
