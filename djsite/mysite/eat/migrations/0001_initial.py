# Generated by Django 4.0.2 on 2022-04-19 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('description', models.CharField(default='', max_length=255)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='img/%y')),
            ],
        ),
    ]
