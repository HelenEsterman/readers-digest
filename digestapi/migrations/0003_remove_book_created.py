# Generated by Django 4.2.7 on 2023-11-08 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('digestapi', '0002_book_created_alter_bookcategory_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='created',
        ),
    ]
