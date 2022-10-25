from django.urls import path
from . import views
from rest_framework.authtoken.views import ObtainAuthToken


urlpatterns = [
    path('accounts/', views.ListCreateAccountsView.as_view()),
    path('login/', ObtainAuthToken.as_view()),
    path(
        'accounts/newest/<int:num>/',
        views.ListAccountsByNewestView.as_view()
    ),
    path(
        'accounts/<pk>/',
        views.UpdateAccountView.as_view(),
        name="user_url"
    ),
    path(
        'accounts/<pk>/management/',
        views.UpdateAccountView.as_view()
    )
]
