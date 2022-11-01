# Generated by Django 4.1.1 on 2022-10-30 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dane',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slackUsername', models.CharField(max_length=100)),
                ('backend', models.BooleanField(default=True)),
                ('bio', models.CharField(max_length=400)),
            ],
        ),
    ]