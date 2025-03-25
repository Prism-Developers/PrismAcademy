# Generated by Django 5.1.7 on 2025-03-23 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common_App', '0007_courses_age_courses_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='course_duration',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='courses',
            name='course_overview',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='courses',
            name='requirments',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='courses',
            name='session_duration',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='courses',
            name='what_you_will_learn',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='courses',
            name='age',
            field=models.CharField(choices=[('5-7', '5-7'), ('7-9', '7-9'), ('9-11', '9-11'), ('11+', '11+')], max_length=50, null=True),
        ),
    ]
