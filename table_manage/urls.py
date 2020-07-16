from django.urls import path
from table_manage.views import get_table

urlpatterns = [
    path('', get_table),
]
