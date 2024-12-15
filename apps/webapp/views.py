from django.views.generic import TemplateView

from apps.webapp.models import PermohonanKredensial
from web_project import TemplateLayout

"""
This file is a view controller for multiple pages as a module.
Here you can override the page view layout.
Refer to sample/urls.py file for more pages.
"""


# @login_required
class SampleView(TemplateView):
    # Predefined function
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        return context


class KredensialUpdateView(TemplateView):

    def get_transaction(self, pk):
        return PermohonanKredensial.objects.get(pk=pk)

    def get_context_data(self, **kwargs):
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        context["permohonankredensial_id"] = self.get_transaction(self.kwargs["pk"])
        return context
