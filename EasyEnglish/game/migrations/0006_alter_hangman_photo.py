# Generated by Django 4.1.1 on 2023-02-05 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_rename_type_hangman_types'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hangman',
            name='photo',
            field=models.FileField(null=True, upload_to='audio'),
        ),
    ]
