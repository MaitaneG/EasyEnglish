# Generated by Django 4.1.1 on 2023-02-20 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocabulary', '0003_alter_term_photo'),
        ('user', '0003_rename_appuser_ranking'),
    ]

    operations = [
        migrations.AddField(
            model_name='ranking',
            name='learnt',
            field=models.ManyToManyField(to='vocabulary.term'),
        ),
    ]