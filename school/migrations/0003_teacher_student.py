# Generated by Django 3.1.2 on 2021-05-31 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20210531_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='student',
            field=models.ManyToManyField(related_name='teachers', to='school.Student'),
        ),
    ]
