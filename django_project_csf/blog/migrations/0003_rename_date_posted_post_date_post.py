# Generated by Django 5.1.4 on 2024-12-31 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_date_post_post_date_posted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='date_posted',
            new_name='date_post',
        ),
    ]
