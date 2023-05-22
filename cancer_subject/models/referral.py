from django.db import models

from edc_base.model_mixins import BaseUuidModel
from edc_constants.choices import YES_NO

from ..choices import WHY_REFERRED


class Referral (BaseUuidModel):

    """ CA011 """

    report_datetime = models.DateTimeField(null=True)

    referrals = models.CharField(
        verbose_name=('Have any referrals been made that should '
                      'be reported been made '
                      '(by study team or hospital staff)?'),
        max_length=3,
        choices=YES_NO,
        help_text='(if No , STOP and return form to DMC.)',
    )

    why_referred = models.CharField(
        verbose_name='Where and why has patient been referred?',
        max_length=750,
        choices=WHY_REFERRED,
    )

    referral_date = models.DateTimeField(
        verbose_name='Date of referral?',
        max_length=25,
        help_text='dd/mm/yyyy',
    )

    comments = models.CharField(
        verbose_name='Comments',
        max_length=35,
    )

    class Meta:
        app_label = 'cancer_subject'
        verbose_name = 'Referral'
