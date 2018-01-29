from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, redirect, render

from account.decorators import login_required
from account.models import SignupCode
from pinax.waitinglist.models import WaitingListEntry  # @@@ decouple?

from .forms import CohortCreateForm
from .models import Cohort, SignupCodeCohort


@login_required
@permission_required("cohorts.manage_cohorts")
def cohort_list(request):

    ctx = {
        "cohorts": Cohort.objects.order_by("-created")
    }
    return render(request, "pinax/cohorts/cohort_list.html", ctx)


@login_required
@permission_required("cohorts.manage_cohorts")
def cohort_create(request):

    if request.method == "POST":
        form = CohortCreateForm(request.POST)

        if form.is_valid():
            cohort = form.save()
            return redirect("pinax_cohorts:detail", cohort.id)
    else:
        form = CohortCreateForm()

    ctx = {
        "form": form,
    }
    return render(request, "pinax/cohorts/cohort_create.html", ctx)


@login_required
@permission_required("cohorts.manage_cohorts")
def cohort_detail(request, pk):

    cohort = get_object_or_404(Cohort, pk=pk)

    # people who are NOT invited or on the site already
    waiting_list = WaitingListEntry.objects.exclude(
        email__in=SignupCode.objects.values("email")
    ).exclude(
        email__in=get_user_model().objects.values("email")
    )

    ctx = {
        "cohort": cohort,
        "waiting_list": waiting_list,
    }
    return render(request, "pinax/cohorts/cohort_detail.html", ctx)


@login_required
@permission_required("cohorts.manage_cohorts")
def cohort_member_add(request, pk):

    cohort = Cohort.objects.get(pk=pk)

    if "invite_next" in request.POST:
        try:
            N = int(request.POST["invite_next"])
        except ValueError:
            return redirect("pinax_cohorts:detail", cohort.pk)
        # people who are NOT invited or on the site already
        waiting_list = WaitingListEntry.objects.exclude(
            email__in=SignupCode.objects.values("email")
        ).exclude(
            email__in=get_user_model().objects.values("email")
        )
        emails = waiting_list.values_list("email", flat=True)[:N]
    else:
        email = request.POST["email"].strip()
        if email:
            emails = [email]
        else:
            emails = []

    for email in emails:
        if not SignupCode.objects.filter(email=email).exists():
            signup_code = SignupCode.create(email=email, max_uses=1, expiry=730)
            signup_code.save()
            SignupCodeCohort.objects.create(signup_code=signup_code, cohort=cohort)

    return redirect("pinax_cohorts:detail", cohort.pk)


@login_required
@permission_required("cohorts.manage_cohorts")
def cohort_send_invitations(request, pk):

    cohort = Cohort.objects.get(pk=pk)
    cohort.send_invitations()

    return redirect("pinax_cohorts:detail", cohort.pk)
