# Generated by Django 5.0.6 on 2024-06-15 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='games',
            old_name='data_lancamento',
            new_name='data_de_lancamento',
        ),
    ]