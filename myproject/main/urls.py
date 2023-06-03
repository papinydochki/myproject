from django.urls import path
from . import views
from django.views.generic.base import RedirectView

favicon_view = RedirectView.as_view(url='/static/main/favicon.ico', permanent=True)

urlpatterns = [
    path('', views.index, name='home'),


]
