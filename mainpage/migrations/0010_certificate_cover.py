# Generated by Django 4.0.4 on 2023-06-30 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0009_alter_certificate_pdf'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/'),
        ),
    ]
