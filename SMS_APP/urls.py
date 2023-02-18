from django.contrib import admin
from django.urls import path
from SMS_APP import views

app_name = "sms"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
]
