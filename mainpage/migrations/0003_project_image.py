# Generated by Django 4.0.4 on 2023-05-15 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0002_project_content_project_link_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(default='this is nigeria', upload_to='images/'),
        ),
    ]