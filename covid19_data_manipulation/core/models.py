from django.db import models


class CountryRegion(models.Model):
    country = models.CharField(max_length=30)
    province_state = models.CharField(max_length=30)
    population = models.DecimalField(max_digits=8, decimal_places=2)


class DailyStatistics(models.Model):
    date = models.DateTimeField(auto_now_add=False)
    confirmed = models.IntegerField()
    deaths = models.IntegerField()
    recovered = models.IntegerField()
    active = models.IntegerField()
    country_region = models.OneToOneField(CountryRegion, on_delete=models.CASCADE, primary_key=True)
