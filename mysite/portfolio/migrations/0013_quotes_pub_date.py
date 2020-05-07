# Generated by Django 3.0.5 on 2020-05-06 01:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0012_auto_20200505_0218'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotes',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date_published'),
            preserve_default=False,
        ),
    ]
