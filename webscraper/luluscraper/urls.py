from django.urls import path

from luluscraper import views

urlpatterns = [
    path("scrape", views.scrape, name="scrape"),
]