# Generated by Django 2.2.8 on 2020-04-17 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='legenda',
            field=models.CharField(default='legenda', max_length=200),
        ),
    ]