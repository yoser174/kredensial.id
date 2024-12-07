from django.urls import path
from .views import SampleView


urlpatterns = [
    path(
        "",
        SampleView.as_view(template_name="index.html"),
        name="index",
    ),
    path(
        "kredensial_lists/",
        SampleView.as_view(template_name="kredensial_lists.html"),
        name="kredensial_lists",
    ),
]
