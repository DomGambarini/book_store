from django.db import models


class Category(models.Model):
    """Category Models"""

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    FICTION = 'Fiction'
    NON_FICTION = 'Non-Fiction'
    CHILDREN_AND_TEENS = 'Children and Teens'

    CATEGORY_CHOICES = [
        (FICTION, 'Fiction'),
        (NON_FICTION, 'Non-Fiction'),
        (CHILDREN_AND_TEENS, 'Children and Teens'),
    ]

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        " Method to return category's friendly name "
        return self.friendly_name


class Product(models.Model):
    """Product Models"""
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=254)
    author = models.CharField(max_length=254)
    publication_date = models.DateField(null=True, blank=True, help_text="Enter the publication date in the format YYYY-MM-DD.")
    number_of_pages = models.PositiveIntegerField()
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    sku = models.CharField(max_length=254, null=True, blank=True)
    isbn = models.CharField(max_length=13, null=True, blank=True)

    def __str__(self):
        return self.title
