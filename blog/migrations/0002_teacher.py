# Generated by Django 4.2.4 on 2023-08-19 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
