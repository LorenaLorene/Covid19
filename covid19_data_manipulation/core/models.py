from django.db import models


class CountryRegion(models.Model):
    country = models.CharField(max_length=30)
    province_state = models.CharField(max_length=30, null=True, blank=True)
    population = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)


class DailyStatistics(models.Model):
    date = models.DateTimeField(auto_now_add=False)
    confirmed = models.IntegerField(null=True, blank=True)
    deaths = models.IntegerField(null=True, blank=True)
    recovered = models.IntegerField(null=True, blank=True)
    active = models.IntegerField(null=True, blank=True)
    country_region = models.OneToOneField(CountryRegion, on_delete=models.CASCADE, primary_key=True)
