# Generated by Django 3.0.5 on 2020-05-05 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_resume_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resume',
            old_name='resume',
            new_name='pdf',
        ),
    ]
