# Generated by Django 4.2.11 on 2024-04-11 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataapp', '0003_alter_scrapingdata_hotel_number_of_reviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='scrapingdata',
            name='executions_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
