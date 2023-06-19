from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.sign_in, name="login"),
    path("logout/", views.sign_out, name="logout"),
    path("pricing/", views.pricing, name="pricing"),
    path("register/", views.register, name="register"),
    path("user/", views.user, name="user"),
    path("update/", views.update, name="update"),
    path("new-record/", views.new_record, name="new-record"),
]
