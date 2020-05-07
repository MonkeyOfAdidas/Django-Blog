# Generated by Django 3.0.5 on 2020-04-24 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_comment_comment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='about_user',
            field=models.TextField(blank=True, verbose_name='About user'),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=120, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, verbose_name='First name'),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, verbose_name='Last name'),
        ),
    ]