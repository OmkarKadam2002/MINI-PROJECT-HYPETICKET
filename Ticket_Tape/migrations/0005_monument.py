# Generated by Django 3.0.5 on 2022-11-12 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ticket_Tape', '0004_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Monument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Monument_name', models.CharField(max_length=100)),
                ('Monument_location', models.CharField(max_length=100)),
                ('Monument_city', models.CharField(max_length=100)),
                ('Monument_image', models.ImageField(upload_to='')),
            ],
        ),
    ]
