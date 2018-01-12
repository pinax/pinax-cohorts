import collections

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from account.models import SignupCode, SignupCodeResult

Member = collections.namedtuple("Member", ["email", "signup_code", "user", "invited"])


@python_2_unicode_compatible
class Cohort(models.Model):

    name = models.CharField(_("name"), max_length=35)
    created = models.DateTimeField(_("created"), default=timezone.now, editable=False)

    class Meta:
        permissions = (
            ("manage_cohorts", "Can manage cohorts"),
        )

    def members(self):
        members = []
        for scc in self.signupcodecohort_set.select_related():
            try:
                scr = SignupCodeResult.objects.get(signup_code=scc.signup_code_id)
            except SignupCodeResult.DoesNotExist:
                user = None
            else:
                user = scr.user
            members.append(
                Member(
                    scc.signup_code.email,
                    scc.signup_code,
                    user,
                    bool(scc.signup_code.sent)
                )
            )
        return members

    def member_counts(self):
        members = self.members()
        return {
            "total": len(members),
            "users": len([m for m in members if m.user is not None]),
            "pending": len([m.signup_code for m in members if not m.invited]),
        }

    def send_invitations(self):
        for sc in [m.signup_code for m in self.members() if not m.invited]:
            sc.send()

    def __str__(self):
        return self.name


class SignupCodeCohort(models.Model):
    """
    fetch cohort of a given signup code
        SignupCodeCohort.objects.select_related(
            "cohort"
        ).get(
            signup_code__code="abc"
        ).cohort

    list of people waiting NOT on the site already or invited
        WaitingListEntry.objects.exclude(
            email__in=SignupCode.objects.values("email")
        ).exclude(
            email__in=User.objects.values("email")
        )
    """
    signup_code = models.OneToOneField(SignupCode, on_delete=models.CASCADE)
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)


class UserCohort(models.Model):
    """
    Upon signup we create an instance of this model associating the new user
    and their cohort
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
