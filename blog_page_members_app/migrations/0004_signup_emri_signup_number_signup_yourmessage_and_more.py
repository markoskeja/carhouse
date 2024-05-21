# Generated by Django 5.0.6 on 2024-05-14 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_page_members_app', '0003_signup'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='emri',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='signup',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='signup',
            name='yourmessage',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='signup',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]