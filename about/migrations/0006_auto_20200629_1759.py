# Generated by Django 3.0.7 on 2020-06-29 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0005_auto_20200629_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(max_length=1500),
        ),
    ]