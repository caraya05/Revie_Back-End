import os

from django.db import models
from django.utils.translation import gettext_lazy as _
from loducode_utils.models.audit import Audit

from reviews.managers.reviewer_manager import ReviewerManager


def create_path_reviewer(instance, filename):
    return os.path.join(
        instance.name, instance.lastname,
        filename
    )


class Reviewer(Audit):
    model_name = 'Reviewer'

    name: str = models.CharField(verbose_name=_('Name'), max_length=555)
    lastname: str = models.CharField(verbose_name=_('Last Name'), max_length=555)
    age: int = models.IntegerField(verbose_name=_('Age'), default='0')
    gender: str = models.CharField(verbose_name=_('Gender'), max_length=3)
    phone: str = models.CharField(verbose_name=_('Phone'), max_length=10)
    photo: str = models.ImageField(verbose_name=_('Photo'), upload_to=create_path_reviewer, blank=True, null=True)
    description: str = models.TextField(verbose_name=_('Description'), null=True, blank=True)

    objects = ReviewerManager()

    class Meta(Audit.Meta):
        verbose_name = _('Reviewer')
        verbose_name_plural = _('Reviewers')

    def __str__(self):
        return f'{self.name} {self.lastname}'

    @staticmethod
    def autocomplete_search_fields():
        return 'name', 'lastname'
