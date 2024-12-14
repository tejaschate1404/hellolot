from django.urls import path
from testApp.views import testCode
from testApp.views import services
from .import views



urlpatterns = [
     path("testcode/",testCode),
     path("newservices/",services),
     path('add-category/', views.add_category, name='add_category'),
     path('add-service/', views.add_service, name='add_service'),
     path('view-services/', views.view_services, name='view_services'),
   
]
