# Generated by Django 4.0.7 on 2022-11-22 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0008_rename_requirement_money'),
    ]

    operations = [
        migrations.CreateModel(
            name='link_amount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('ifsc', models.CharField(max_length=150)),
                ('state', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
                ('dob', models.CharField(max_length=150)),
                ('number', models.CharField(max_length=150)),
                ('type', models.CharField(max_length=150)),
                ('cash', models.CharField(max_length=150)),
            ],
        ),
    ]
