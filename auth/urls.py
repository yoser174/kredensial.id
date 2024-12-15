from django.urls import path

from auth.views import LoginView


urlpatterns = [
    path(
        "login/",
        LoginView.as_view(template_name="login.html"),
        name="login",
    ),
]
