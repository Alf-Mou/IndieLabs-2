# Generated by Django 5.0.6 on 2024-06-12 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('mini_descricao', models.TextField(max_length=200)),
                ('imagem_destaque', models.ImageField(upload_to='fotos/')),
                ('imagem_miniatura', models.ImageField(upload_to='fotos/')),
                ('descricao_completa', models.TextField(max_length=2000)),
                ('imagem_gameplay1', models.ImageField(upload_to='fotos/')),
                ('imagem_gameplay2', models.ImageField(upload_to='fotos/')),
                ('imagem_gameplay3', models.ImageField(upload_to='fotos/')),
                ('imagem_gameplay4', models.ImageField(upload_to='fotos/')),
                ('imagem_solta', models.ImageField(upload_to='fotos/')),
                ('data_lancamento', models.CharField(max_length=50)),
                ('desenvolvedor', models.CharField(max_length=50)),
                ('estudio', models.CharField(max_length=50)),
            ],
        ),
    ]
