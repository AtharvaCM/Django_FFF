# Generated by Django 3.1 on 2020-09-21 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fff', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default_user.svg', upload_to='profile_pics'),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
