from django.db import models
from datetime import date
# from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _

class BuildingCategory(models.Model):
    building_code = models.CharField(max_length=50)
    building_adress = models.CharField(max_length=50)

    def __str__(self):
        return self.building_code

class ApartmentCategory(models.Model):
    building_code = models.ForeignKey(BuildingCategory, on_delete=models.CASCADE)
    apartment_num = models.CharField(max_length=50)
    apartment_owner = models.CharField(max_length=50)
    def __str__(self):
        return self.apartment_num

class Lietotaji(models.Model):
    lietotajs = models.CharField(max_length=50)
    apartment_tag = models.ManyToManyField(ApartmentCategory)

class WaterCounterCategory(models.Model):
    apartment_num = models.ForeignKey(ApartmentCategory, on_delete=models.CASCADE)
    water_counter_num = models.CharField(max_length=50)

    WATER_COUNTER_TYPE_CHOICES = (
        ('CW', 'Cold water'),
        ('HW', 'Hot water')
         )
    water_counter_type = models.CharField(
        max_length=5,
        choices=WATER_COUNTER_TYPE_CHOICES,
        default='CW',
    )
    water_counter_setup_date = models.DateField(_("Date"), default=date.today)
    water_counter_expiration_date = models.DateField()
    water_counter_active = models.BooleanField(default=True)

    def __str__(self):
        return self.water_counter_num

class WaterCounterReadings(models.Model):
    water_counter_num = models.ForeignKey(WaterCounterCategory, on_delete=models.CASCADE)
    water_counter_reading = models.DecimalField(max_digits=8, decimal_places=3)
    # water_counter_readings_date_on = models.DateField()
    water_counter_readings_current_date = models.DateField(default=date.today)
    # water_counter_submitted_by_user = AbstractUser.username
    # logged_user = self.form_class(instance=self.request.user, initial={'email':self.request.user.email})
    # def __str__(self):
    #     return self.water_counter_reading


