# Generated by Django 2.2.3 on 2019-07-30 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tows', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pilot',
            name='DPI',
            field=models.CharField(help_text='Enter your DPI', max_length=13),
        ),
    ]