# Generated by Django 3.0.5 on 2022-10-02 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email_id', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=100)),
                ('message', models.TextField(default='abc')),
            ],
        ),
    ]