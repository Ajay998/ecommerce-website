from django.urls import path, include
# from core.views import index
from core import views

app_name = "core"

urlpatterns = [
     path("ecommerce/", views.index)
     
]

