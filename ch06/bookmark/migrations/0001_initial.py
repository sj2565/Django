# Generated by Django 3.2.7 on 2021-09-15 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, verbose_name='TITLE')),
                ('url', models.URLField(unique=True, verbose_name='URL')),
            ],
        ),
    ]
