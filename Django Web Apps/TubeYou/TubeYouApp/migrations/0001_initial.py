# Generated by Django 2.0.3 on 2018-10-26 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VideoInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vidName', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=1000)),
            ],
        ),
    ]
