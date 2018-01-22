from django.conf.urls import include


urlpatterns = [
    (r"^", include("pinax.cohorts.urls", namespace="pinax_cohorts")),
]
