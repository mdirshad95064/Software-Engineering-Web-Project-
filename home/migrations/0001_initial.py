# Generated by Django 4.0.6 on 2022-07-27 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='media')),
                ('description', models.TextField(blank=True)),
                ('rank', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='media')),
                ('slug', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('slug', models.CharField(max_length=500)),
                ('icon', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='media')),
                ('description', models.TextField(blank=True)),
                ('url', models.URLField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('slug', models.CharField(max_length=500)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('price', models.IntegerField()),
                ('discounted_price', models.IntegerField()),
                ('image', models.ImageField(upload_to='media')),
                ('description', models.TextField(blank=True)),
                ('specification', models.TextField(blank=True)),
                ('stock', models.CharField(choices=[('in', 'In Stock'), ('out', 'Out of Stock')], max_length=100)),
                ('labels', models.CharField(blank=True, choices=[('new', 'new'), ('hot', 'hot'), ('sale', 'sale'), ('', 'default')], max_length=100)),
                ('Subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.subcategory')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
        ),
    ]
