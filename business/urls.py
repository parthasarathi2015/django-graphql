from django.urls import path
from .views import (
    business_list,
    business_detail,
    business_create,
    business_update,
    business_delete
)

urlpatterns = [
    path('', business_list, name='business_list'),
    path('<int:pk>/', business_detail, name='business_detail'),
    path('create/', business_create, name='business_create'),
    path('<int:pk>/update/', business_update, name='business_update'),
    path('<int:pk>/delete/', business_delete, name='business_delete'),
]

