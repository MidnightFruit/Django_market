from django.urls import path
from catalog.views import ContactsListView, HomeListView, ProductTemplateView, ProductCreateViews, ProductDeleteView, \
    ProductUpdateView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', ContactsListView.as_view(), name='contacts'),
    path('', HomeListView.as_view(), name='home'),
    path('product/<int:pk>/', ProductTemplateView.as_view(), name='product'),
    path('create_product/', ProductCreateViews.as_view(), name='create_product'),
    path('delete_product/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('update_product/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
]
