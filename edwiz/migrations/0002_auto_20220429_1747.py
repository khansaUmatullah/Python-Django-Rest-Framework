# Generated by Django 3.1.4 on 2022-04-29 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edwiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.CharField(max_length=30),
        ),
    ]
