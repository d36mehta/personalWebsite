# Generated by Django 3.0.5 on 2020-05-06 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0014_languages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='languages',
            name='languages',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
