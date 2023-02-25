# Generated by Django 4.1.5 on 2023-02-15 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_ass_cover'),
    ]

    operations = [
        migrations.CreateModel(
            name='exx',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('owner', models.CharField(max_length=100)),
                ('pdf', models.FileField(upload_to='notes/pdfs/')),
                ('cover', models.ImageField(blank=True, null=True, upload_to='notes/covers/')),
            ],
        ),
    ]