# Generated by Django 3.0.7 on 2020-08-09 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_auto_20200719_2156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='items',
        ),
    ]
