import os
from typing import Optional

from django.db import models
from django.utils.translation import gettext_lazy as _
from loducode_utils.models.audit import Audit

from reviews.managers.restaurant_manager import RestaurantManager


def create_path_photo_restaurant(instance, filename):
    full_name = str(instance.restaurant.name) + '' + str(instance.restaurant.date_create)
    return os.path.join(
        full_name,
        filename
    )


class PhotoRestaurant(Audit):
    model_name = 'PhotoRestaurant'
    restaurant: Optional = models.ForeignKey(to='reviews.restaurant', verbose_name='Restaurant',
                                             on_delete=models.CASCADE)
    photo_one: str = models.ImageField(verbose_name=_('Photo One'), upload_to=create_path_photo_restaurant, blank=True,
                                       null=True)
    photo_two: str = models.ImageField(verbose_name=_('Photo Two'), upload_to=create_path_photo_restaurant, blank=True,
                                       null=True)
    photo_three: str = models.ImageField(verbose_name=_('Photo Three'), upload_to=create_path_photo_restaurant,
                                         blank=True, null=True)
    photo_four: str = models.ImageField(verbose_name=_('Photo Four'), upload_to=create_path_photo_restaurant,
                                        blank=True, null=True)
    photo_five: str = models.ImageField(verbose_name=_('Photo Five'), upload_to=create_path_photo_restaurant,
                                        blank=True, null=True)

    objects = RestaurantManager()

    class Meta(Audit.Meta):
        verbose_name = _('Photo Restaurant')
        verbose_name_plural = _('Photos Restaurants')

    def __str__(self):
        return f'{self.restaurant}'

    @staticmethod
    def autocomplete_search_fields():
        return 'restaurant'
