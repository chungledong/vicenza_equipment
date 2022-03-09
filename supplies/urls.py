from django.urls import path
from .views import (
    homeView,
    SuppliesDetailView,
    GroupSuppliesListView,
    SuppliesListView,
    SuppliesListViewByGroup,
)

app_name = 'supplies'
urlpatterns = [
    path('', homeView, name='home'),
    path('detail/<pk>/',SuppliesDetailView.as_view(),name='detail'),
    path('groupsupplies-view/', GroupSuppliesListView.as_view(), name='groupsupplies-view'),
    path('supplies-view/', SuppliesListView.as_view(), name='supplies-view'),
    path('list-supplies/<pk>/', SuppliesListViewByGroup.as_view(),name='list-supplies'),
]
