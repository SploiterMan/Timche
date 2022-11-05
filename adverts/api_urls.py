from django.urls import path
from .api_views import *


urlpatterns = [
    # Adverts
    path('list/waiting/', WaitingAdvertsList.as_view()),
    path('list/confirmed/', ConfirmedAdvertsList.as_view()),
    path('confirm/<int:pk>/', ConfirmAdvert.as_view()),
    path('auther/list/', ConfirmedAdvertsAutherList.as_view()),
    path('auther/waiting/', WaitingAdvertsAutherList.as_view()),
    path('update/<int:pk>/', AdvertUpdate.as_view()),
    path('<int:pk>/', AdvertViewOrDestroy.as_view()),
    path('create/', CreateAdvert.as_view()),
    path('list/', AdvertList.as_view()),
]
