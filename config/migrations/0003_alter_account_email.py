# Generated by Django 4.1.2 on 2022-10-14 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0002_rename_sociallink_socialuserlink'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(blank=True, max_length=150, unique=True),
        ),
    ]
