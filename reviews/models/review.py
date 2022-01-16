import os
from datetime import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _
from loducode_utils.models.audit import Audit

from reviews.managers.review_manager import ReviewManager


def create_path_review(instance, filename):
    return os.path.join(
        instance.name,
        filename
    )


class Review(Audit):
    model_name = 'Review'

    score1 = '1'
    score2 = '2'
    score3 = '3'
    score4 = '4'
    score5 = '5'

    SCORE_CHOICES = [
        ('1', score1),
        ('2', score2),
        ('3', score3),
        ('4', score4),
        ('5', score5)
    ]

    title: str = models.CharField(verbose_name=_('Title'), max_length=555)
    date: datetime = models.DateField()
    description: str = models.TextField(verbose_name=_('Description'))
    score_service: str = models.CharField(verbose_name=_('Score Service'), max_length=5, choices=SCORE_CHOICES,
                                          default='0')
    score_food: str = models.CharField(verbose_name=_('Score Food'), max_length=5, choices=SCORE_CHOICES,
                                       default='0')
    score_environment: str = models.CharField(verbose_name=_('Score Environment'), max_length=5, choices=SCORE_CHOICES,
                                              default='0')
    score_quality_price: str = models.CharField(verbose_name=_('Score Quality Price'), max_length=5,
                                                choices=SCORE_CHOICES, default='0')
    objects = ReviewManager()

    class Meta(Audit.Meta):
        verbose_name = "Review"
        verbose_name_plural = "Reviews"

    def __str__(self):
        return f'{self.title} {self.date}'

    @staticmethod
    def autocomplete_search_fields():
        return 'title'
