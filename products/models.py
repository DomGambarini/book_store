from django.db import models


class Category(models.Model):
    """Category Models"""
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        " Method to return category's friendly name "
        return self.friendly_name


class Product(models.Model):
    """Product Models"""
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    title = models.CharField(max_length=254)
    author = models.CharField(max_length=254)
    publication_date = models.DateField(null=True, blank=True)
    number_of_pages = models.PositiveIntegerField()
    new_arrival = models.BooleanField(blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    isbn = models.CharField(max_length=13, null=True, blank=True)
    by_age = models.CharField(max_length=8, choices=[
        ("children", "children"), ("teens", "teens"), ("adult", "adult"), ("all", "all")])

    def __str__(self):
        return self.title
