# Generated by Django 3.1.4 on 2022-04-29 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edwiz', '0002_auto_20220429_1747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='enrolled_sourses',
        ),
        migrations.AddField(
            model_name='student',
            name='enrolled_courses',
            field=models.ManyToManyField(to='edwiz.course'),
        ),
    ]
