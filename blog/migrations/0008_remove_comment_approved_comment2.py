# Generated by Django 2.0 on 2019-01-18 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_comment_approved_comment2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='approved_comment2',
        ),
    ]