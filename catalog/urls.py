from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import ContactsListView, HomeListView, ProductTemplateView, ProductCreateViews, ProductDeleteView, \
    ProductUpdateView, CategoryListView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', ContactsListView.as_view(), name='contacts'),
    path('', HomeListView.as_view(), name='home'),
    path('product/<int:pk>/', cache_page(60)(ProductTemplateView.as_view()), name='product'),
    path('create_product/', ProductCreateViews.as_view(), name='create_product'),
    path('delete_product/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('update_product/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('categories/', CategoryListView.as_view(), name='categories/')
]
