from django.contrib import admin
from django.urls import path
from .views import CustomLoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CustomLoginView.as_view(), name='admin_login'),
]
