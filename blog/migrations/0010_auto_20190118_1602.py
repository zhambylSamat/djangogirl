# Generated by Django 2.0 on 2019-01-18 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_comment_approved_comment3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='approved_comment3',
            field=models.BooleanField(default=False),
        ),
    ]
