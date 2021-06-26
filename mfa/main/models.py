# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.urls import reverse

User = get_user_model()

def get_product_url(obj, viewname, model_name):
    ct_model = obj.__class__._meta.model_name
    return reverse(viewname, kwargs={'ct_model': ct_model, 'slug': obj.slug})


class LetestProductManager:

    @staticmethod
    def get_products_for_main_page(*args, **kwargs):
        with_respect_to=kwargs.get('with respect to')
        products = []
        ct_models = ContentType.objects.filter(model_in=args)
        for ct_model in ct_models:
            model_products = ct_model.model_class()._base_manager.all().older_by('-id')[:5]
            products.extend(model_products)
        if with_respect_to:
            ct_model = ContentType.objects.fiter(model=with_respect_to)
            if ct_model.exists():
                if with_respect_to in args:
                    return sorted(
                        products, key=lambda x: x.__class__.__meta.startswith(with_respect_to), reverse=True
                        )
        return products


class LatestProducts:

    objects = LetestProductManager()


class Category(models.Model):

    name = models.CharField(max_length=255, verbose_name='Имя категории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):

    class Meta:
        abstract = True

    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.title


class Moloko(Product):

    belki = models.CharField(max_length=255, verbose_name='Белки')
    giry = models.CharField(max_length=255, verbose_name='Жиры')
    voda = models.CharField(max_length=255, verbose_name='Вода')


    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

class Yaico(Product):

    belki = models.CharField(max_length=255, verbose_name='Белки')
    giry = models.CharField(max_length=255, verbose_name='Жиры')
    voda = models.CharField(max_length=255, verbose_name='Вода')


    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)


    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Ourdt(models.Model):

    title = models.CharField(max_length=255, verbose_name='Наименование')
    image = models.ImageField(verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание', null=True)

    def __str__(self):
        return self.title