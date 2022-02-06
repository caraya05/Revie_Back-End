from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from users.managers.person_manager import PersonManager


class Person(AbstractUser):
    model_name = 'Person'
    username = None
    email = models.EmailField('email address', unique=True)
    rol: str = models.CharField(verbose_name='Rol',
                                max_length=10, help_text='Reviewer = RW, Restaurant = RT',
                                null=False, blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['rol', ]

    objects = PersonManager()

    class Meta:
        verbose_name = _('Person')
        verbose_name_plural = _('Persons')

    def __str__(self):
        return f'{self.email}'

    @staticmethod
    def autocomplete_search_fields():
        return 'email'
