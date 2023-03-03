
from django.urls import path, include

urlpatterns = [
    path("django-rq/", include("django_rq.urls")),
]