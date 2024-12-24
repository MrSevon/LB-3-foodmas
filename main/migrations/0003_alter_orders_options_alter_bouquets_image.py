# Generated by Django 5.1.3 on 2024-12-15 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_orders_alter_bouquets_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orders',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказов'},
        ),
        migrations.AlterField(
            model_name='bouquets',
            name='image',
            field=models.ImageField(upload_to='bouquets/', verbose_name='Изображение'),
        ),
    ]
