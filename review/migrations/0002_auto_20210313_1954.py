# Generated by Django 3.1.7 on 2021-03-13 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='Question',
            field=models.IntegerField(blank=True, choices=[(1, '매우아니다'), (2, '아니다'), (3, '보통'), (4, '그렇다'), (5, '매우그렇다')]),
        ),
    ]
