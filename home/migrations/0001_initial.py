# Generated by Django 4.2.7 on 2024-02-27 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bible',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.CharField(max_length=15)),
                ('chapter', models.IntegerField()),
                ('verse', models.IntegerField()),
            ],
        ),
    ]
