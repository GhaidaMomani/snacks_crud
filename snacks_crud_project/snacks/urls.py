from django.urls import path

from .views import (HomeView,
                    SnacksCreateView,
                    SnacksDetailView,
                    SnacksUpdateView,
                    SnacksDeleteView
                    )

urlpatterns = [
    path('', HomeView.as_view(), name = "home"),
    path('create/', SnacksCreateView.as_view(), name = "create"),
    path('detail/<int:pk>', SnacksDetailView.as_view(), name = "detail"),
    path('update/<int:pk>', SnacksUpdateView.as_view(), name = "update"),
    path('delete/<int:pk>', SnacksDeleteView.as_view(), name = "delete"),
] 