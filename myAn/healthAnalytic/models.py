from healthAnalytic import init_import
from django.db import models


# Create your models here.
class Country(models.Model):
    country_name = models.CharField(max_length=255, blank=False, null=False)
    country_code = models.CharField(max_length=5, blank=False, null=True)

    def __str__(self):
        return self.country_region_name


class Kid(models.Model):
    last_name = models.CharField(max_length=255, blank=False, null=False)
    first_name = models.CharField(max_length=255, blank=False, null=False)
    birth_date = models.DateField(verbose_name="Birth Date", blank=True, null=True)
    birth_place = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Activity(models.Model):
    activity_name = models.CharField(max_length=30, blank=False, null=False)
    calculation_mass = models.CharField(max_length=15, blank=False, null=False)


class InformationPerPeriod(models.Model):
    kid = models.ForeignKey(Kid, blank=False, on_delete=models.CASCADE)
    date = models.DateField(verbose_name="Date", blank=False, null=False)
    from_to = models.CharField(max_length=255, blank=True, null=False)
    activity = models.ForeignKey(Activity, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False)
    comment = models.CharField(max_length=255, blank=True, null=False)