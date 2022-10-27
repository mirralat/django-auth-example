
from django.contrib import admin
from django.urls import path


from demouser.views import *

urlpatterns = [
    path('admin/',admin.site.urls),
    path("", homepage, name="homepage"),
    path("register/", register_request, name="register"),
    path("login/", login_request, name="login"),
    path("logout/", logout_request, name="logout"),
]
