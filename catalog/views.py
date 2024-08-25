from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version, Category
from catalog.services import get_categories_from_cache


class ProductCreateViews(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy("users:login")
    redirect_field_name = "redirect_to"
    model = Product
    success_url = reverse_lazy('catalog:home')
    form_class = ProductForm

    def form_valid(self, form):
        product = form.save()
        product.seller = self.request.user
        product.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        return context_data


class ProductUpdateView(LoginRequiredMixin, UpdateView):

    login_url = reverse_lazy("users:login")
    redirect_field_name = "redirect_to"
    model = Product
    fields = ('name', 'description', 'preview', 'category', 'price', )

    def get_context_data(self, **kwargs):
        user = self.request.user
        if user.has_perm("catalog.change_product") or self.object.seller == user:
            context_data = super().get_context_data(**kwargs)
            VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
            context_data['formset'] = VersionFormset()
            if self.request.method == 'POST':
                context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
            else:
                context_data['formset'] = VersionFormset(instance=self.object)
            return context_data
        else:
            raise PermissionDenied

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:home')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy("users:login")
    redirect_field_name = "redirect_to"
    model = Product
    success_url = reverse_lazy('catalog:home')


class ContactsListView(ListView):
    template_name = "catalog/contacts_list.html"

    def get(self, request):
        return render(request, self.template_name)


class HomeListView(ListView):
    template_name = "catalog/home_list.html"
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        versions_dict = {}
        # versions = Version.objects.filter(current_version=True)
        for product in Product.objects.all():
            for version in Version.objects.all():
                if version.current_version:
                    if version.product_id == int(product.pk):
                        versions_dict[version.product_id] = version.version_name
        context_data['versions'] = versions_dict
        return context_data


class ProductTemplateView(TemplateView):
    template_name = "catalog/product.html"

    def get(self, request, pk):
        context = {'object': Product.objects.get(pk=pk)}
        return render(request, self.template_name, context)


class CategoryListView(ListView):
    model = Category

    def get_queryset(self):
        return get_categories_from_cache()
