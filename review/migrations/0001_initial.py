# Generated by Django 3.1.7 on 2021-03-13 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=200)),
                ('Question', models.IntegerField(blank=True, choices=[(1, '매우아니다'), (2, '아니다'), (3, '보통'), (4, '그렇다'), (5, '매우그렇다')], null=True)),
                ('D_result', models.IntegerField(null=True)),
            ],
        ),
    ]