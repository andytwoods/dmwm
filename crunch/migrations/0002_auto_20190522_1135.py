# Generated by Django 2.2.1 on 2019-05-22 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crunch', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='zohoinfo',
            name='First_Name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='zohoinfo',
            name='Job_Title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
