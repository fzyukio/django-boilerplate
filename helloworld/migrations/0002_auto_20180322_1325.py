# Generated by Django 2.0.3 on 2018-03-22 00:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='name',
            new_name='content',
        ),
    ]
