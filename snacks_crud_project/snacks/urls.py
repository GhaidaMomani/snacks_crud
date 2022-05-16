from django.urls import path
from .views import (HomeView,
                    SnacksCreateView,
                    SnacksDetailView,
                    SnacksUpdateView,
                    # SnacksDeleteView
                    )

urlpatterns = [
    path('', HomeView.as_view(), name = "home"),
    path('create/', SnacksCreateView.as_view(), name = "create_thing"),
    path('<int:pk>', SnacksDetailView.as_view(), name = "detail_thing"),
    path('update/<int:pk>', SnacksUpdateView.as_view(), name = "update_thing"),
    # path('delete/<int:pk>', SnacksDeleteView.as_view(), name = "delete_thing"),
]