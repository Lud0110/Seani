# Generated by Django 4.2.1 on 2024-02-29 17:05

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='module',
            options={'verbose_name': 'módulo', 'verbose_name_plural': 'módulos'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'pregunta', 'verbose_name_plural': 'preguntas'},
        ),
        migrations.RenameField(
            model_name='question',
            old_name='aswer1',
            new_name='answer1',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='aswer2',
            new_name='answer2',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='aswer3',
            new_name='answer3',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='aswer4',
            new_name='answer4',
        ),
        migrations.RemoveField(
            model_name='question',
            name='image_text',
        ),
        migrations.AddField(
            model_name='question',
            name='question_image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Imagen de la pregunta'),
        ),
        migrations.AlterField(
            model_name='module',
            name='description',
            field=models.CharField(max_length=100, verbose_name='Descripcion del modulo'),
        ),
        migrations.AlterField(
            model_name='module',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Nombre del modulo'),
        ),
        migrations.AlterField(
            model_name='question',
            name='correct',
            field=models.CharField(max_length=5, verbose_name='Respuesta Correcta'),
        ),
    ]
