# Generated by Django 5.1.3 on 2024-11-12 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_id', models.TextField()),
                ('pet_type', models.TextField()),
                ('pet_breed', models.TextField()),
                ('pet_price', models.IntegerField()),
                ('offer_price', models.IntegerField()),
                ('img', models.FileField(upload_to='')),
                ('dis', models.TextField()),
            ],
        ),
    ]