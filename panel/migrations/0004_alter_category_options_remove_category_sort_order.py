# Generated by Django 4.2.3 on 2023-12-23 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0003_alter_category_options_category_sort_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={},
        ),
        migrations.RemoveField(
            model_name='category',
            name='sort_order',
        ),
    ]