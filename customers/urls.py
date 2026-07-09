from django.urls import path
from . import views


urlpatterns = [

    path(
        'start-project/',
        views.customer_form,
        name='customer_form'
    ),

]
