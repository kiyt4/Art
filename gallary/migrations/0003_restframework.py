# Generated by Django 3.2.9 on 2022-02-28 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallary', '0002_category_order_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='restframework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=223)),
            ],
        ),
    ]
