# Generated by Django 4.0.4 on 2022-05-11 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ownership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('badge', models.CharField(max_length=100)),
                ('date_now', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
