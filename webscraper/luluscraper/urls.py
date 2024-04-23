from django.urls import path
from luluscraper import views

urlpatterns = [
    #API routes
    path("scrape", views.scrape, name="scrape"),
]