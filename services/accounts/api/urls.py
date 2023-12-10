from django.contrib.auth.views import LogoutView
from django.urls import include, path

# from . import views


urlpatterns = [
    path('accounts/logout', LogoutView.as_view()),
    path(
        'accounts/auth/',
        include('djoser.social.urls')
    ),
    # path(
    #     'accounts/profile/',
    #     views.RedirectSocial.as_view()
    # ),
]
