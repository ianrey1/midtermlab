# customers/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.CustomerListView.as_view(), name='customer-list'),  # Make sure this is correct
    path('create/', views.CustomerCreateView.as_view(), name='customer-create'),
    path('<int:pk>/', views.CustomerDetailView.as_view(), name='customer-detail'),
    path('<int:pk>/update/', views.CustomerUpdateView.as_view(), name='customer-update'),
    path('<int:pk>/delete/', views.CustomerDeleteView.as_view(), name='customer-delete'),
]
