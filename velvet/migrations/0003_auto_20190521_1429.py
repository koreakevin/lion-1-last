# Generated by Django 2.2.1 on 2019-05-21 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('velvet', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='Comment_text',
            new_name='comment_text',
        ),
    ]
