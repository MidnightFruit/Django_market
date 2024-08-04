from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.TextField(verbose_name="название категории")
    description = models.TextField(verbose_name="описание категории")

    def __str__(self):
        return f"{self.name}\t{self.description}"

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = "категории"
        ordering = ("name",)


class Product(models.Model):
    name = models.TextField(verbose_name="название продукта")
    description = models.TextField(verbose_name="описание продукта")
    preview = models.ImageField(upload_to="media/", verbose_name="превью продукта")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name="категория продукта")
    price = models.IntegerField(verbose_name="цена продукта")
    created_at = models.DateField(verbose_name="дата создания продукта", auto_now_add=True)
    updated_at = models.DateField(verbose_name="дата редактирования продукта", auto_now=True)
    manufactured_at = models.DateField(verbose_name='Дата производства продукта', null=True)

    def __str__(self):
        return f'{self.name}\t{self.description}\t{self.price}\t{self.created_at}\t{self.updated_at}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = "продукты"
        ordering = ('name', 'category',)


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="продукт")
    version = models.IntegerField(verbose_name="номер версии")
    version_name = models.CharField(max_length=255, verbose_name="название версии")
    current_version = models.BooleanField(verbose_name="признак текущей версии")

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = "версии"
        ordering = ('product', 'version', 'current_version',)
