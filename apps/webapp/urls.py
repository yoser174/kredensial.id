from django.urls import path
from django.contrib.auth.decorators import login_required

from apps.webapp.pages.permohonankredensial.view import (
    PermohonanKredensialAddView,
    PermohonanKredensialListView,
    update_profile,
)
from .views import SampleView


urlpatterns = [
    path(
        "",
        login_required(SampleView.as_view(template_name="index.html")),
        name="index",
    ),
    path(
        "permohonankredensial/list/",
        login_required(
            PermohonanKredensialListView.as_view(
                template_name="permohonankredensial_lists.html"
            )
        ),
        name="permohonankredensial",
    ),
    path(
        "permohonankredensial/add/",
        login_required(
            PermohonanKredensialAddView.as_view(
                template_name="permohonankredensial_add.html"
            )
        ),
        name="transactions-add",
    ),
    path(
        "htmx/update_profile",
        login_required(update_profile),
        name="htmx_update_profile",
    ),
]
