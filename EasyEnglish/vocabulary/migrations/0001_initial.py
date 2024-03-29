# Generated by Django 4.1.1 on 2023-02-17 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vocabulary',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('word', models.CharField(max_length=50)),
                ('types', models.CharField(choices=[('Animal', 'Animal'), ('Food', 'Food'), ('Furniture', 'Furniture'), ('School material', 'School material')], max_length=50)),
                ('spanish', models.CharField(max_length=100)),
                ('photo', models.ImageField(null=True, upload_to='')),
                ('audio', models.FileField(null=True, upload_to='audio')),
            ],
        ),
    ]
