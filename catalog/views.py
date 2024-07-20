from django.shortcuts import render
from django.views.generic import ListView, View, TemplateView
# from django.views import


from catalog.models import Product


class ContactsListView(View):
    template_name = "catalog/contacts.html"

    def get(self, request):
        return render(request, self.template_name)


# def contacts(request):
#     return render(request,
#                   "catalog/contacts.html")
#
#

class HomeListView(ListView):
    template_name = "catalog/home.html"
    model = Product
    def get(self, request):
        context = {'object': Product.objects.all()}
        return render(request, self.template_name, context)

# def home(request):
#     context = {"object": Product.objects.all()}
#     return render(request,
#                   'catalog/home.html', context=context)


class ProductTemplateView(TemplateView):
    template_name = "catalog/product.html"

    def get(self, request, pk):
        context = {'object': Product.objects.get(pk=pk)}
        return render(request, self.template_name, context)


# def product(request, pk):
#     context = {"object": Product.objects.get(pk=pk)}
#     return render(request,
#                   'catalog/product.html', context)
