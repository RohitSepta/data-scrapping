from django.db import models


class ScrapingData(models.Model):
    hotel_name = models.CharField(max_length=200, null=True, blank=True)
    hotel_exact_address = models.CharField(max_length=200, null=True, blank=True)
    hotel_headline_rating = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    hotel_number_of_reviews = models.CharField(max_length=200, null=True, blank=True)
    executions_time = models.DateTimeField(null=True, blank=True, auto_now_add=True)

    def __str__(self):
        return self.hotel_name if self.hotel_name else "Scraping Data"
