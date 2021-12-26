# from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('signup/', views.signup),
    # path('api-token-auth/', obtain_jwt_token),
    path('<str:username>/', views.getUser, name='getUser'),
    path('changeadmin/<str:username>/', views.changeAdmin, name='changeAdmin'),
]
