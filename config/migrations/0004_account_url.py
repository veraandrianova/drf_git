# Generated by Django 4.1.2 on 2022-10-14 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0003_alter_account_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='url',
            field=models.URLField(blank=True, max_length=100),
        ),
    ]
