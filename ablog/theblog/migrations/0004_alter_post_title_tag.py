# Generated by Django 4.0.6 on 2022-07-29 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0003_alter_post_title_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default=models.CharField(max_length=255), max_length=255),
        ),
    ]
