from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register/', views.register , name='register'),
    path('login/', views.login_view , name='login'),
    path('dashboard/', views.dashboard , name='dashboard'),
    path('logout',views.logout,name = "logout" ),
    #urls for sending messages
    path('send_message/', views.send_message, name='send_message'),
    path('check_messages/', views.check_messages, name='check_messages'),
    path('patients/',views.patients,name='patients'),
    path('service_providers/',views.service_providers,name="service_providers"),
    path('retrieve_history/',views.retrieve_history,name="retrieve_history"),
    path('search/',views.search,name="search")
]

