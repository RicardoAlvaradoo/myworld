# Generated by Django 4.1.2 on 2022-10-28 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('descrip', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
