from django.db import models


class Capacity(models.Model):
    capacities = models.CharField(max_length=50)

    def __str__(self):
        return self.capacities


class CPU(models.Model):
    cpus = models.CharField(max_length=50)

    def __str__(self):
        return self.cpus


class Authentication(models.Model):
    authentications = models.CharField(max_length=50)

    def __str__(self):
        return self.authentications


class Color(models.Model):
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.color


class Out_Camera(models.Model):
    ability = models.CharField(max_length=50)

    def __str__(self):
        return self.ability


class DeviceModel(models.Model):
    name = models.CharField(max_length=50)
    display_size = models.DecimalField(decimal_places=1, max_digits=2)
    gram = models.CharField(max_length=10, default=True)
    capacity = models.ManyToManyField('Capacity')
    home_button = models.CharField(max_length=3)
    cpu = models.ForeignKey('CPU', on_delete=models.CASCADE)
    authentication = models.ForeignKey('Authentication', on_delete=models.CASCADE)
    release_date = models.CharField(max_length=50)
    color = models.ManyToManyField('Color',)
    in_camera = models.CharField(max_length=50)
    out_camera = models.ManyToManyField('Out_Camera')

    class Meta:
        db_table = "device"

    def __str__(self):
        return self.name


class Price(models.Model):
    price = models.CharField(max_length=50)
