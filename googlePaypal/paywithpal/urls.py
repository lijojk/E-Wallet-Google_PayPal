from django.urls import path
from .views import sanboxpayment
urlpatterns = [
    path('payment/', sanboxpayment, name='sanboxpayment'),

]
