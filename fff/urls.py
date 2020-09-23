from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views

# app_name = 'fff'

# this module contains the links on the landing page and the overview of the app

urlpatterns = [
    path('', views.index, name='freshfromfarm-home'),
    path('home/', views.index, name='freshfromfarm-home'),
    path('about/', views.about, name='freshfromfarm-about'),
    path('services/', views.services, name='freshfromfarm-services'),
    path('contact/', views.contact, name='freshfromfarm-contact'),
    # path('accounts/', include('django.contrib.auth.urls')),

    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('accounts/profile/', views.view_profile, name='view_profile'),
    path('accounts/profile/edit/', views.edit_profile, name='edit_profile'),

    path('accounts/password_change/',
         auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('accounts/password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('accounts/password_reset/',
         auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),

    path('register/', views.register, name='register'),
    path('accounts/activate/<uidb64>/<token>/',
         views.activate, name='activate'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
