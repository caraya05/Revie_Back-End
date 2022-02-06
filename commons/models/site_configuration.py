import os

from django.db import models
from django.utils.translation import gettext as _
from geoposition.fields import GeopositionField
from solo.models import SingletonModel


def create_path_category(instance, filename):
    return os.path.join(
        str('image-default'),
        filename
    )


class SiteConfigurationM(SingletonModel):
    """Singleton admin site.
            Common elements to render in the project, according to its needs.

           :param SingletonModel: Instance handling class for singleton pattern.
           :type SingletonModel: class.
           :returns: por si la necesitamos.
        """
    page_facebook_url: str = models.CharField(verbose_name=_('Page of Facebook'), max_length=255, blank=True, null=True,
                                              default='#')
    """Page for url redirection of facebook"""
    page_twitter_url: str = models.CharField(verbose_name=_('Page of Twitter'), max_length=255, blank=True, null=True,
                                             default='#')
    """Page for url redirection of twitter"""
    page_instagram_url: str = models.CharField(verbose_name=_('Page of Instagram'), max_length=255, blank=True,
                                               null=True, default='#')
    """Page for url redirection of instagram"""
    location: GeopositionField = GeopositionField(verbose_name=_('Location'), blank=True, null=True)
    """store the coordinates of the main office of the project contact us"""
    image: str = models.ImageField(
        verbose_name=_('Icon'), upload_to=create_path_category, blank=True, null=True
    )
    """project manager image or icon"""

    def __str__(self):
        return "Site Configuration"

    class Meta:
        verbose_name = _("Site Configuration")
        verbose_name_plural = _('Site Configurations')
