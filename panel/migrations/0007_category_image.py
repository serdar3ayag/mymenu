# Generated by Django 5.0 on 2023-12-26 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0006_alter_dish_options_remove_dish_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]
