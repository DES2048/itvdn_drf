from django.urls import path
from .views import CarCreateView, CarListView, CarDetailView

urlpatterns = [
    path("create/", CarCreateView.as_view()),
    path("all/", CarListView.as_view()),
    path("detail/<int:pk>/", CarDetailView.as_view()),
]
