# Generated by Django 4.1.5 on 2023-02-11 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_ass_todo'),
    ]

    operations = [
        migrations.AddField(
            model_name='ass',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='notes/covers/'),
        ),
    ]