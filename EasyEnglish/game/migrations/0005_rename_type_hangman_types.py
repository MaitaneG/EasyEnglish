# Generated by Django 4.1.1 on 2023-01-21 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_alter_hangman_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hangman',
            old_name='type',
            new_name='types',
        ),
    ]
