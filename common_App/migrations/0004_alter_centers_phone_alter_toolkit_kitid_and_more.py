# Generated by Django 5.1.6 on 2025-05-18 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common_App', '0003_alter_courses_level_alter_courses_maxnmberofstudents_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='centers',
            name='phone',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='toolkit',
            name='kitID',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='toolkit',
            name='level',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='toolkit',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
