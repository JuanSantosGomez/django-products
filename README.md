# Products

Products is a Django app to store product ID and Description information. For each product description, a product Barcode is assigned to it.

# Quick start

---

- 1. Add "products" to your INSTALLED_APPS setting like this::

  INSTALLED_APPS = [
  ...
  'products',
  ]

- 2. Include the products URLconf in your project urls.py like this::

  path('products/', include('products.urls')),

- 3. Run `python manage.py migrate` to create the products models.
