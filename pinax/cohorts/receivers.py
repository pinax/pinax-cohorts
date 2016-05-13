from django.dispatch import receiver

from account.signals import user_signed_up

from .models import SignupCodeCohort, UserCohort


@receiver(user_signed_up)
def handle_user_signup(sender, **kwargs):
    signup_code = kwargs["form"].cleaned_data["code"]
    # fetch the cohort for the signup code
    qs = SignupCodeCohort.objects.select_related("cohort")
    try:
        cohort = qs.get(signup_code__code=signup_code).cohort
        # create a UserCohort for user association to a cohort
        UserCohort.objects.create(user=kwargs["user"], cohort=cohort)
    except SignupCodeCohort.DoesNotExist:
        pass
