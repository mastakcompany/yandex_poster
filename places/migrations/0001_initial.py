# Generated by Django 4.2.5 on 2023-10-04 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description_short', models.CharField(max_length=255)),
                ('description_long', models.TextField()),
                ('lng', models.CharField(max_length=100)),
                ('lat', models.CharField(max_length=100)),
            ],
        ),
    ]
