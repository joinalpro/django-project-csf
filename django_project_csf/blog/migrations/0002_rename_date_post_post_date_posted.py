# Generated by Django 5.1.4 on 2024-12-31 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='date_post',
            new_name='date_posted',
        ),
    ]