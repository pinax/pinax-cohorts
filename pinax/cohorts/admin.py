from django.contrib import admin

from .models import Cohort, SignupCodeCohort, UserCohort


class SignupCodeCohortInline(admin.TabularInline):

    model = SignupCodeCohort


class UserCohortInline(admin.TabularInline):

    model = UserCohort


admin.site.register(
    Cohort,
    inlines=[
        SignupCodeCohortInline,
        UserCohortInline,
    ]
)
