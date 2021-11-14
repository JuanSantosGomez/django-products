from re import I
from rest_framework import routers, urlpatterns
from products.api import ProductViewSet
from .views import PostMultiple
from django.urls import path

router = routers.DefaultRouter()
router.register("api/products", ProductViewSet, "products")
urlpatterns = [
    path("api/multiupload", PostMultiple.as_view()),
]
urlpatterns += router.urls
