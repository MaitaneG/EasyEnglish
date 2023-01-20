# Generated by Django 4.1.1 on 2023-01-08 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_rename_appuser_hangman'),
    ]

    operations = [
        migrations.AddField(
            model_name='hangman',
            name='photo',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='hangman',
            name='type',
            field=models.CharField(choices=[('Animal', 'Animal'), ('Food', 'Food'), ('Furniture', 'Furniture'), ('School material', 'School material')], max_length=50),
        ),
    ]