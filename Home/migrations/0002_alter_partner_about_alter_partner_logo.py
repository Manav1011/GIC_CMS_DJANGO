# Generated by Django 5.0.6 on 2024-07-09 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='about',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='partner',
            name='logo',
            field=models.FileField(upload_to=''),
        ),
    ]
