# Generated by Django 4.0.4 on 2022-07-06 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0008_userprofile_pronouns'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]