from django.conf.urls import url

from . import views

app_name = "pinax_cohorts"

urlpatterns = [
    url(r"^$", views.cohort_list, name="list"),
    url(r"^create/$", views.cohort_create, name="create"),
    url(r"^cohort/(\d+)/$", views.cohort_detail, name="detail"),
    url(r"^cohort/(\d+)/add_member/$", views.cohort_member_add, name="member_add"),
    url(r"^cohort/(\d+)/send_invitations/$", views.cohort_send_invitations, name="send_invitations"),
]
