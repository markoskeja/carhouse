# Generated by Django 5.0.6 on 2024-05-10 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_page_members_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
