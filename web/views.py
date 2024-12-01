from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from web.forms import LoginForm


def index(request):
    template = loader.get_template("web/index.html")
    context = {}
    return HttpResponse(template.render(context, request))


def login_page(request):
    logout(request)
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        print("username :" + username)
        print("password :" + password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("OK")
            login(request, user)
            return redirect("/web")
        else:
            messages.add_message(
                request, messages.ERROR, "Incorect username and/or password"
            )
    template = loader.get_template("web/pages/login.html")
    login_form = LoginForm()
    context = {"form": login_form}
    return HttpResponse(template.render(context, request))
