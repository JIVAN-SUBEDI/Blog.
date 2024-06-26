# Generated by Django 5.0.1 on 2024-06-06 05:14

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_categories_slug_posts'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='categories',
            new_name='Category',
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('image', models.ImageField(upload_to='posts/')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('desc', ckeditor.fields.RichTextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('categories', models.ManyToManyField(related_name='posts', to='blog.category')),
            ],
        ),
        migrations.DeleteModel(
            name='posts',
        ),
    ]
