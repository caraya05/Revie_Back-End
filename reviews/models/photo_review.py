import os
from typing import Optional

from django.db import models
from django.utils.translation import gettext_lazy as _
from loducode_utils.models.audit import Audit

from reviews.managers.photo_review_manager import PhotoReviewManager


def create_path_photo_review(instance, filename):
    full_name = str(instance.review.title) + '' + str(instance.review.date)
    return os.path.join(
        full_name,
        filename
    )


class PhotoReview(Audit):
    model_name = 'PhotoReview'
    review: Optional = models.ForeignKey(to='reviews.review', verbose_name='Review',
                                         on_delete=models.CASCADE)
    photo_one: str = models.ImageField(verbose_name=_('Photo One'), upload_to=create_path_photo_review, blank=True,
                                       null=True)
    photo_two: str = models.ImageField(verbose_name=_('Photo Two'), upload_to=create_path_photo_review, blank=True,
                                       null=True)
    photo_three: str = models.ImageField(verbose_name=_('Photo Three'), upload_to=create_path_photo_review,
                                         blank=True, null=True)

    objects = PhotoReviewManager()

    class Meta(Audit.Meta):
        verbose_name = "Photo Review"
        verbose_name_plural = "Photos Reviews"

    def __str__(self):
        return f'{self.review}'

    @staticmethod
    def autocomplete_search_fields():
        return 'review'
