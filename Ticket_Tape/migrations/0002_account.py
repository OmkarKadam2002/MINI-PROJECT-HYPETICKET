# Generated by Django 3.0.5 on 2022-10-05 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ticket_Tape', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email_id', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('conpassword', models.CharField(max_length=100)),
            ],
        ),
    ]
