# Generated by Django 4.1.7 on 2023-08-17 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyApi', '0002_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='about',
            field=models.TextField(),
        ),
    ]