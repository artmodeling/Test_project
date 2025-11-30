from django.urls import path

from test_project.views import home_view

urlpatterns = [
  path("", home_view)
]
