# Generated by Django 3.1.7 on 2021-06-12 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10000)),
                ('email', models.EmailField(max_length=1000)),
                ('password', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=10000000)),
            ],
        ),
    ]
