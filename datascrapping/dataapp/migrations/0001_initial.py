# Generated by Django 4.2.11 on 2024-04-10 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScrapingData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(blank=True, max_length=200, null=True)),
                ('hotel_exact_address', models.CharField(blank=True, max_length=200, null=True)),
                ('hotel_headline_rating', models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True)),
                ('hotel_number_of_reviews', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
    ]
