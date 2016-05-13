import importlib

from django.apps import AppConfig as BaseAppConfig
from django.utils.translation import ugettext_lazy as _


class AppConfig(BaseAppConfig):

    name = "pinax.cohorts"
    label = "pinax_cohorts"
    verbose_name = _("Pinax Cohorts")

    def ready(self):
        importlib.import_module("pinax.cohorts.receivers")
