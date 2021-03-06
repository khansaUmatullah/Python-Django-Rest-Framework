# Generated by Django 3.1.4 on 2022-04-29 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=20)),
                ('source', models.CharField(max_length=20)),
                ('course_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=20)),
                ('student_id', models.IntegerField()),
                ('enrolled_sourses', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='edwiz.course')),
            ],
        ),
    ]
