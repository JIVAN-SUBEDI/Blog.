# Generated by Django 5.0.1 on 2024-06-06 09:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_recommended_posts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommended_posts',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post', unique=True),
        ),
    ]
