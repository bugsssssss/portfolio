# Generated by Django 4.1.7 on 2023-03-21 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_projects'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='decription',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='projects',
            name='author',
            field=models.CharField(blank=True, max_length=50, verbose_name='author'),
        ),
    ]
