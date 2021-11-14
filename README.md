# django-products

![example workflow](https://github.com/juansantosgomez/django-products/actions/workflows/python-publish.yml/badge.svg)
![example workflow](https://github.com/juansantosgomez/django-products/actions/workflows/test-python-publish.yml/badge.svg)

##### current version: v0.3

Products is a Django app to store product ID and Description information. For each product description, a product Barcode is assigned to it. The product model in this app is an accessible API governed by generic ViewSet and Default Routers.

#### REQUIREMENTS:

- Python v3.9
- pip
- Django v3.2

#### INSTALLATION:

On your command line inside your project directory type the following:

```
pip install django-products
```

#### QUICK START

- Add "products" to your INSTALLED_APPS setting like this::

```
INSTALLED_APPS = [
...
'products',
]
```

- Include the products URLconf in your project urls.py like this::

```
path('products/', include('products.urls')),
```

- Run `python manage.py migrate` to create the products models.

#### USAGE
