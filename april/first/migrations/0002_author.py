# Generated by Django 4.1.6 on 2023-04-25 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('age', models.PositiveIntegerField()),
                ('active_date', models.DateField()),
                ('penname', models.CharField(max_length=150)),
                ('journal', models.CharField(max_length=150)),
            ],
        ),
    ]
