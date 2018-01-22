from django.conf.urls import include, url

urlpatterns = [
    url(r"^", include("pinax.cohorts.urls", namespace="pinax_cohorts")),
]
