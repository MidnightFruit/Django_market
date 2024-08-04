from django import forms

from catalog.models import Product, Version


class ProductForm(forms.ModelForm):
    banned_words = ['казино', 'криптовалюта', 'крипта', 'биржа',
                    'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        for word in self.banned_words:
            if word in cleaned_data:
                raise forms.ValidationError("Ваше название включает в себя запрещённые на данном сайте слова")
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        for word in self.banned_words:
            if word in cleaned_data:
                raise forms.ValidationError("В описании содержатся запрещённые на данном сайте слова")
        return cleaned_data


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
        