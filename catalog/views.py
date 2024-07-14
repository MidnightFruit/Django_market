from django.shortcuts import render

from catalog.models import Product


def contacts(request):
    return render(request,
                  "catalog/contacts.html")


def home(request):
    context = {"object": Product.objects.all()}
    return render(request,
                  'catalog/home.html', context=context)


def product(request, pk):
    context = {"object": Product.objects.get(pk=pk)}
    return render(request,
                  'catalog/product.html', context)
