from django.urls import path
from testApp.views import testCode



urlpatterns = [
     path("testcode/",testCode),
   
]
