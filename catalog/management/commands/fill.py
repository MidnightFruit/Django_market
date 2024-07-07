from django.core.management import BaseCommand

from catalog.models import Category, Product
import json

class Command(BaseCommand):
    @staticmethod
    def json_read_categories():
        with open('data/categories_data.json') as file:
            temp = json.load(file)
        return temp

    @staticmethod
    def json_read_products():
        with open('data/products_data.json') as file:
            temp = json.load(file)
        return temp

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()
        product_for_create = []
        category_for_create = []
        for category in Command.json_read_categories():
            category_for_create.append(Category(name=category['name'], description=['description']))

        Category.objects.bulk_create(category_for_create)
        category_for_create.clear()

        for product in Command.json_read_products():
            product_for_create.append(
                Product(name=product['name'],
                        description=product['description'],
                        preview=product['preview'],
                        category=Category.objects.get(pk=product['category']),
                        price=product['price'],
                        created_at=product['created_at'],
                        updated_at=product['updated_at'],
                        manufactured_at=product['manufactured_at'])
            )
        Product.objects.bulk_create(product_for_create)
