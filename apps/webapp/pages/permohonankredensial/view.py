from datetime import date

from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView
from django_htmx.middleware import HtmxDetails

from apps.webapp.forms import IdentitasNakesForm, PermohonanKredensialForm
from apps.webapp.models import IdentitasNakes, PermohonanKredensial, ProfesiNakes
from web_project import TemplateLayout


class PermohonanKredensialListView(TemplateView):

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        # transactions = self.get_annotated_transactions()
        # Update the context
        context.update(
            {
                # "transactions": transactions,
                # "transactions_count": PermohonanKredensial.objects.count(),
                # "due_count": self.get_total_due(),
                # "paid_count": self.get_total_paid(),
                # "canceled_count": self.get_total_canceled(),
            }
        )
        # TemplateHelper.map_context(context)
        return context

    # def get_annotated_transactions(self):
    #     # Get all transactions and order them by ID
    #     return PermohonanKredensial.objects.all().order_by("id")

    # def get_total_due(self):
    #     total_due_amount = PermohonanKredensial.objects.filter(status="Due").aggregate(
    #         total_due=Sum("total")
    #     )
    #     return (
    #         float(total_due_amount["total_due"])
    #         if total_due_amount["total_due"] is not None
    #         else 0.0
    #     )

    # def get_total_paid(self):
    #     # Calculate the total sum of 'total' field for 'Paid' transactions
    #     total_paid_amount = PermohonanKredensial.objects.filter(
    #         status="Paid"
    #     ).aggregate(total_paid=Sum("total"))
    #     return (
    #         float(total_paid_amount["total_paid"])
    #         if total_paid_amount["total_paid"] is not None
    #         else 0.0
    #     )

    # def get_total_canceled(self):
    #     total_canceled_amount = PermohonanKredensial.objects.filter(
    #         status="Canceled"
    #     ).aggregate(total_canceled=Sum("total"))
    #     return (
    #         float(total_canceled_amount["total_canceled"])
    #         if total_canceled_amount["total_canceled"] is not None
    #         else 0.0
    #     )


class PermohonanKredensialAddView(TemplateView):
    # permission_required = "transactions.add_transaction"

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context["current_date"] = date.today().strftime("%Y-%m-%d")
        context["user"] = User.objects.get(id=self.request.user.id)
        context["identitas_nakes"] = IdentitasNakes.objects.filter(
            user=self.request.user
        )[0]
        print(context["identitas_nakes"])
        context["profesi_nakes_lists"] = ProfesiNakes.objects.all()
        return context

    def post(self, request):
        form = PermohonanKredensialForm(request.POST)
        if form.is_valid():
            if not self.transaction_exists(form.cleaned_data):
                form.save()
                messages.success(request, "Transaction Added")
            else:
                messages.error(request, "Transaction already exists")
        else:
            messages.error(request, "Transaction Failed")
        return redirect("permohonankredensial")

    def transaction_exists(self, cleaned_data):
        return PermohonanKredensial.objects.filter(
            customer__iexact=cleaned_data["customer"],
            transaction_date=cleaned_data["transaction_date"],
            due_date=cleaned_data["due_date"],
            total=cleaned_data["total"],
            status=cleaned_data["status"],
        ).exists()


# Typing pattern recommended by django-stubs:
# https://github.com/typeddjango/django-stubs#how-can-i-create-a-httprequest-thats-guaranteed-to-have-an-authenticated-user
class HtmxHttpRequest(HttpRequest):
    htmx: HtmxDetails


@require_POST
def update_profile(request: HtmxHttpRequest) -> HttpResponse:
    form = IdentitasNakesForm(request.POST)
    userObj = User.objects.get(id=request.user.id)
    identitasNakesObj = IdentitasNakes.objects.get_or_create(user=userObj)[0]
    if form.is_valid():
        first_name = form.cleaned_data["first_name"]
        last_name = form.cleaned_data["last_name"]
        userObj.first_name = first_name
        userObj.last_name = last_name
        userObj.save()
        date_of_birth = form.cleaned_data["date_of_birth"]
        profesi_nakes = form.cleaned_data["profesi_nakes"]
        nip_nps = form.cleaned_data["nip_nps"]
        place_of_birth = form.cleaned_data["place_of_birth"]
        address = form.cleaned_data["address"]
        no_ijazah = form.cleaned_data["no_ijazah"]
        no_str = form.cleaned_data["no_str"]
        no_sip = form.cleaned_data["no_sip"]
        starting_work = form.cleaned_data["starting_work"]
        mobile_phone = form.cleaned_data["mobile_phone"]
        identitasNakesObj.profesi_nakes = ProfesiNakes.objects.get(id=profesi_nakes)
        identitasNakesObj.date_of_birth = date_of_birth
        identitasNakesObj.nip_nps = nip_nps
        identitasNakesObj.place_of_birth = place_of_birth
        identitasNakesObj.address = address
        identitasNakesObj.mobile_phone = mobile_phone
        identitasNakesObj.no_ijazah = no_ijazah
        identitasNakesObj.no_str = no_str
        identitasNakesObj.no_sip = no_sip
        identitasNakesObj.starting_work = starting_work
        identitasNakesObj.save()
        print(identitasNakesObj)
    return render(
        request,
        "update_profile.html",
        {
            "form": form,
        },
    )
