# Generated by Django 4.2.1 on 2023-05-15 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150, verbose_name='ФИО автора')),
                ('author_image', models.ImageField(upload_to='', verbose_name='Изображение автора')),
                ('birth_date', models.DateField(verbose_name='Дата рождения')),
            ],
        ),
        migrations.CreateModel(
            name='BookGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('book_image', models.ImageField(upload_to='', verbose_name='Изображение книги')),
                ('release_date', models.DateField(verbose_name='Дата выпуска')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_site.author')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_site.bookgenre')),
            ],
        ),
    ]
