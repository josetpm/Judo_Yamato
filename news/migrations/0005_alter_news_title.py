# Generated by Django 5.1.1 on 2024-10-03 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_news_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.TextField(max_length=50),
        ),
    ]
