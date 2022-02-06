from datetime import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _
from geoposition.fields import GeopositionField
from loducode_utils.models.audit import Audit

from reviews.managers.restaurant_manager import RestaurantManager


class Restaurant(Audit):
    model_name = 'Restaurant'

    name: str = models.CharField(verbose_name=_('Name'), max_length=555)
    nit: str = models.CharField(verbose_name=_('NIT'), max_length=20)
    phone: str = models.CharField(verbose_name=_('Phone'), max_length=10)
    location: GeopositionField = GeopositionField(verbose_name=_('Location'), blank=True, null=True)
    website: str = models.CharField(verbose_name=_('Web Site'), max_length=100, blank=True, null=True)
    description: str = models.TextField(verbose_name=_('Description'), null=True, blank=True)
    score: str = models.CharField(verbose_name=_('Score'), max_length=10, blank=True, null=True, default='0')
    date_create: datetime = models.DateField(verbose_name=_('Date Create'))

    objects = RestaurantManager()

    class Meta(Audit.Meta):
        verbose_name = _('Restaurant')
        verbose_name_plural = _('Restaurants')

    def __str__(self):
        return f'{self.name}'

    @staticmethod
    def autocomplete_search_fields():
        return 'name'
