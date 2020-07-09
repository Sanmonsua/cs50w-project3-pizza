# Generated by Django 3.0.7 on 2020-07-09 03:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('smallPrice', models.FloatField()),
                ('largePrice', models.FloatField()),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('dishes', models.ManyToManyField(blank=True, related_name='toppings', to='orders.Dish')),
            ],
        ),
    ]