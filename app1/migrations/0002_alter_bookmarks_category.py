# Generated by Django 4.0.2 on 2022-02-03 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmarks',
            name='category',
            field=models.CharField(max_length=20),
        ),
    ]
