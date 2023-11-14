
from django.urls import path 
from .import views
urlpatterns = [
    path('',views.HomeApiView.as_view(),name='home'),
    path('login/',views.LoginApiView.as_view(),name='login'),
    path('register/',views.RegisterApiView.as_view(),name='register')

]