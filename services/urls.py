from django.urls import path
from services.views import details_Web_Development, services



urlpatterns = [
     path("services/",services),
     path("services/Web_Development",details_Web_Development),
]
