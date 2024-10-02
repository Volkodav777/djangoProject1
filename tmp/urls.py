from django.urls import path
from tmp.views import index, catalog, catalog_2

urlpatterns = [
    path ('', index),
    path ('catalog/', catalog),
    path ('catalog_2/', catalog_2)

]