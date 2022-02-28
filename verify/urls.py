
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.send)
#   path('otpnumbe',views.send)
#   path('',views.home)
]
