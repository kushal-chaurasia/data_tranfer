# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class unique_district(models.Model):
    id = models.AutoField(primary_key=True)
    district_name = models.CharField(blank=True, null=True,max_length=100)
    alias = models.TextField(blank=True, null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'apptraffic_unique_district'


class model_attributes(models.Model):
    id = models.AutoField(primary_key=True)
    maid_count = models.PositiveIntegerField()
    male_count = models.PositiveIntegerField()
    female_count = models.PositiveIntegerField()
    aff_high_count = models.PositiveIntegerField()
    aff_medium_count = models.PositiveIntegerField()
    aff_low_count = models.PositiveIntegerField()
    mean_maid_count = models.FloatField()
    std_maid_count = models.FloatField()
    peak_npeak_count = models.PositiveIntegerField()
    mean_weekday_sum = models.FloatField()
    wkday_pedestrian = models.PositiveIntegerField()
    wkday_vehicle_count = models.PositiveIntegerField()
    wkday_sum = models.PositiveIntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    perdestrian_fac = models.FloatField() 
    hatch_fac = models.FloatField()
    suv_fac = models.FloatField()
    sedan_fac = models.FloatField()
    two_wheel_fac = models.FloatField()
    three_wheel_fac = models.FloatField()
    bus_fac = models.FloatField()
    truck_fac = models.FloatField()
    city = models.CharField(max_length=100)
    district_id = models.ForeignKey(unique_district, on_delete=models.CASCADE)


class npr_calculation(models.Model):
    id = models.AutoField(primary_key=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.PositiveIntegerField()
    Days = models.PositiveIntegerField()
    maid_count = models.CharField(max_length=100)