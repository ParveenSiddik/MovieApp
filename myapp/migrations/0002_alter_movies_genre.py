# Generated by Django 5.1 on 2024-09-04 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='genre',
            field=models.CharField(choices=[('Thriller', 'Thriller'), ('Action', 'Action'), ('Scifi', 'Scifi')], max_length=200),
        ),
    ]
