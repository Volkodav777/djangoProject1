from django.urls import path
from tmp3.views import catalog_6, catalog_7, catalog_9

urlpatterns = [
    path ('catalog_6/', catalog_6),
    path ('catalog_7/', catalog_7),
    path ('catalog_9/', catalog_9),

]