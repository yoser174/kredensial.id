from datetime import date
from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic import TemplateView
from apps.webapp.forms import PermohonanKredensialForm
from apps.webapp.models import PermohonanKredensial
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
        return redirect("transactions")

    def transaction_exists(self, cleaned_data):
        return PermohonanKredensial.objects.filter(
            customer__iexact=cleaned_data["customer"],
            transaction_date=cleaned_data["transaction_date"],
            due_date=cleaned_data["due_date"],
            total=cleaned_data["total"],
            status=cleaned_data["status"],
        ).exists()
