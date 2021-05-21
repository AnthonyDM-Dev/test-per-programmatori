from django.urls import path
from .views import (
    form_view,
    staff_view,
)

urlpatterns = [
    path('form/', form_view, name='form-view'),
    path('staff/', staff_view, name='staff-view'),
]