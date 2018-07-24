# Generated by Django 2.0.5 on 2018-07-23 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_mutual'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investment',
            name='acquired_value',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='investment',
            name='recent_value',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='stock',
            name='purchase_price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='stock',
            name='shares',
            field=models.FloatField(),
        ),
    ]
