from rest_framework_jwt.views import obtain_jwt_token

from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.signup),
    path('api-token-auth/', obtain_jwt_token),
    path('<str:username>/', views.user, name='user'),
    # path('userlist/', views.userlist, name='userlist'),

    # path('user/', views.user)
]
