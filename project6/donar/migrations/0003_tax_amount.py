# Generated by Django 4.0.7 on 2022-11-24 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donar', '0002_donor_purpose'),
    ]

    operations = [
        migrations.CreateModel(
            name='tax_amount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=150)),
            ],
        ),
    ]
