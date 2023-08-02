from django.urls import path, include

urlpatterns = [
    path('accounts/',include('allauth.urls')),
    path('',include('custom_admin.urls')),
    path('sanpay/',include('paywithpal.urls')),


]
