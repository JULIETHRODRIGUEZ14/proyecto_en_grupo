# Generated by Django 4.2.1 on 2023-06-22 22:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='Phone',
            new_name='phone',
        ),
    ]
