# Generated by Django 4.0 on 2021-12-30 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='djangoClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(blank=True, default='', max_length=50)),
                ('Course_Number', models.IntegerField(blank=True, default=0, max_length=50)),
                ('Instructor_Name', models.CharField(blank=True, default='', max_length=50)),
                ('Duration', models.FloatField(blank=True, default=0.0, max_length=10)),
            ],
        ),
    ]