from django.urls import path
from tmp2.views import catalog_3, catalog_4, catalog_5

urlpatterns = [

    path ('catalog_3/', catalog_3),
    path ('catalog_4/', catalog_4),
    path ('catalog_5/', catalog_5),

]