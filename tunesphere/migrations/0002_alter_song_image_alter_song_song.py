# Generated by Django 5.0.3 on 2024-03-15 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunesphere', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='image',
            field=models.ImageField(upload_to='Docs'),
        ),
        migrations.AlterField(
            model_name='song',
            name='song',
            field=models.FileField(upload_to='Docs'),
        ),
    ]
