from django.urls import path
from catalog.views import ContactsListView, HomeListView, ProductTemplateView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', ContactsListView.as_view(), name='contacts'),
    path('', HomeListView.as_view(), name='home'),
    path('product/<int:pk>/', ProductTemplateView.as_view(), name='product')
]