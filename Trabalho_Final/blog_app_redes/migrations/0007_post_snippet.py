# Generated by Django 4.0 on 2022-01-26 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app_redes', '0006_post_header_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Clique Abaixo..', max_length=255),
        ),
    ]