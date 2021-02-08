from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from core import views
from core.customer import views as customer_views
from core.courier import views as courier_views

customer_urlpatters = [
    path('', customer_views.customer_page, name='home'),
    path('profile/', customer_views.profile_page, name='profile'),
]

courier_urlpatters = [
    path('', courier_views.courier_page, name='home'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('social_django.urls', namespace='social')),
    path('', views.home),

    path('login/', auth_views.LoginView.as_view(template_name="login.html")),
    path('logout/', auth_views.LogoutView.as_view(next_page="/")),
    path('register/', views.register_page),
    path('customer/', include((customer_urlpatters, 'customer'))),
    path('courier/', include((courier_urlpatters, 'courier'))),
]
