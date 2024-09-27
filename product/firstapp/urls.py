from django.urls import path
from . import views
from .views import login_view, forgot_password, dashboard, logout_view
from .views import CustomPasswordResetView
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView 
from .views import verify_otp


urlpatterns = [
    path('',views.index, name='index'), 
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('forgot_password/', forgot_password, name='forgot_password'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logout_view, name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('forgot_password/', CustomPasswordResetView.as_view(), name='forgot_password'),  # Forgot password form
    path('password_reset_done/', TemplateView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('verify_otp/', verify_otp, name='verify_otp'),
    
    ]

