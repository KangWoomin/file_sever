# Generated by Django 5.1.1 on 2024-09-10 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=80, verbose_name='email'),
        ),
    ]
