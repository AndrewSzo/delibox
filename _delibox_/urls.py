from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),

    path('login/', auth_views.LoginView.as_view(template_name="login.html")),
    path('logout/', auth_views.LogoutView.as_view(next_page="/")),
    path('customer/', views.customer_page),
    path('courier/', views.courier_page,),
]
