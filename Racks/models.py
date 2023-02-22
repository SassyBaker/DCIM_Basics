from django.db import models

buildings = [
    ('idc', 'IDC 1')
]

voltages = [
    ('ac120', '120v (AC)'),
    ('dc120', '120v (DC)'),
    ('ac208', '208v (AC)'),
    ('dc208', '208v (DC)'),
]


# Create your models here.
class RackModel(models.Model):
    name = models.CharField('Rack', max_length=255)
    ru = models.IntegerField('RUs')

    # Location
    building = models.CharField(max_length=255, null=True, blank=True, choices=buildings, default='idc')
    floor = models.IntegerField(null=True, blank=True)
    sections = models.CharField(max_length=255, null=True, blank=True)  # Cage or Room
    row = models.IntegerField(null=True, blank=True)  # Row or POD

    # Power
    pdus = models.IntegerField('PDUs', null=True, blank=True)
    volts_capacity = models.CharField(max_length=255, null=True, blank=True, choices=voltages, default='ac208')
    amps_capacity = models.IntegerField(null=True, blank=True, default='30')
    total_c13 = models.IntegerField(null=True, blank=True)
    total_c19 = models.IntegerField(null=True, blank=True)
    in_use_c13 = models.IntegerField(null=True, blank=True)
    in_use_c19 = models.IntegerField(null=True, blank=True)

    # Make Model
    manufacturer = models.CharField(max_length=255, null=True, blank=True)
    model = models.CharField(max_length=255, null=True, blank=True)

    # Fiber/Copper Patch's
    # Future feature

    # File upload/Link
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
