# Generated by Django 5.1.1 on 2024-10-03 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_news_upload_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-upload_date'], 'verbose_name': 'news', 'verbose_name_plural': 'news'},
        ),
    ]
