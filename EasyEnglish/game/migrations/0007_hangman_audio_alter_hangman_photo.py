# Generated by Django 4.1.1 on 2023-02-05 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_alter_hangman_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='hangman',
            name='audio',
            field=models.FileField(null=True, upload_to='audio'),
        ),
        migrations.AlterField(
            model_name='hangman',
            name='photo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
