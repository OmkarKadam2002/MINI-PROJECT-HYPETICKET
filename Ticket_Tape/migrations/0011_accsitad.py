# Generated by Django 3.0.5 on 2022-11-29 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ticket_Tape', '0010_tickets_qr_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccSitAd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('monument_name', models.TextField(default='abc')),
            ],
        ),
    ]
