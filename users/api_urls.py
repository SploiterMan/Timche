from django.urls import path
from .api_views import *


urlpatterns = (
    # User
    path('create/', CreateUserByAdmin.as_view()),
    path('manager/create/', CreateUserByUsers.as_view()),
    path('list/', ListUser.as_view()),
    path('update/<slug:phoneNumber>/', UpdateUser.as_view()),
    path('delete/<slug:phoneNumber>/', DeleteUser.as_view()),
    path('<slug:phoneNumber>/', DetailUser.as_view()),

)
