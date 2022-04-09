from django.db import models
import datetime
from django.conf import settings

def year_choices():
    return [(r,r) for r in range(1900, datetime.date.today().year+1)]

class Property(models.Model):
    YEARS = year_choices()
    PROPERTY_PLANIMETRIES = [
        ('1_1', '1 + 1'),
        ('2_1', '2 + 1'),
        ('3_1', '3 + 1'),
        ('DP', 'Duplex'),
        ('VI', 'Villa'),
        ('MS', 'Mansion'),
        ('GR', 'Garage'),
        ]

    address = models.TextField(
        verbose_name='Address of the property',
        null=False,
        blank=False
        )
    planimetry = models.CharField(
        verbose_name='Palnimetry of the property',
        max_length=3,
        choices=PROPERTY_PLANIMETRIES,
        null=False,
        default='1_1'
        )
    size = models.FloatField(
        verbose_name='Size in squared meters',
        null=False,
        blank=False
        )

    price = models.FloatField(
        verbose_name='Price in euros',
        null=False,
        blank=False
        # add constraint for greater than 0
        # add currency conversion
        )
    # add geolocation as a field
    description = models.TextField(
        verbose_name='Desciption for the house',
        null=True,
        blank=True
        )
    city = models.ForeignKey(
        to='City',
        on_delete=models.PROTECT,
        null=False,
        blank=False
        )
    built_year = models.IntegerField(
        verbose_name='Built year',
        choices=YEARS,
        default=datetime.date.today().year,
        null=False,
        blank=False
        )
    floor = models.IntegerField(
        verbose_name='Property floor',
        null=True,
        blank=True
        )
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    class Meta:
        db_table = "property"


class City(models.Model):
    name = models.CharField(
        max_length=15,
        unique=True,
        null=False,
        blank=False
        )
    class Meta:
        db_table = "city"


class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='properties/%Y/%m/%d/', blank=True)
    property = models.ForeignKey(to='Property', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title