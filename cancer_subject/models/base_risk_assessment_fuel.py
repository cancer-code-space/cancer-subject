# coding: utf-8
from django.db import models

from cancer_subject.models.model_mixins.crf_model_mixin import CrfModelMixin
from edc_base.model_fields.custom_fields import OtherCharField
from edc_constants.choices import YES_NO_DONT_KNOW
from cancer_subject.choices.base_risk_assessment import FUEL_HOUSEHOLD20_CHOICE, \
    FUEL_MONTH_CHOICE


class BaseRiskAssessmentFuel (CrfModelMixin):

    fuel_20y = models.CharField(
        verbose_name=("Over the past 20 years, what type of fuel was "
                        "used most for cooking/heating in your household?"),
        max_length=55,
        choices=FUEL_HOUSEHOLD20_CHOICE,
        help_text="",)

    fuel_20y_other = OtherCharField()

    cooking = models.CharField(
        verbose_name=("Over the past 20 years, was cooking usually "
                        "done indoors in your household?"),
        max_length=25,
        choices=YES_NO_DONT_KNOW,
        help_text="",)

    fuel_mm = models.CharField(
        verbose_name=("In the past month, what type of fuel was used "
                        "most for cooking / heating in your household?"),
        max_length=55,
        choices=FUEL_MONTH_CHOICE,
        help_text="",)

    fuel_mm_other = OtherCharField()

    cooking_mm = models.CharField(
        verbose_name=("In the past month, was cooking usually done "
                        "indoors in your household?"),
        max_length=25,
        choices=YES_NO_DONT_KNOW,
        help_text="",)

    class Meta:
        app_label = "cancer_subject"
        verbose_name = "Base Risk Assessment: Fuel"
        verbose_name_plural = "Base Risk Assessment: Fuel"
