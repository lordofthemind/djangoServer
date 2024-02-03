from django.urls import path
from .views import *


urlpatterns = [
    path('', index_view, name='index_view'),
    path('add/', create_user_view, name='create_user_view'),
    path('delete/<pk>/', delete_user_view, name = 'delete_user_view'),
    path('edit/<pk>/', edit_user_view, name='edit_user_view'),

]
