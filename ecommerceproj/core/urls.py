from django.urls import path, include
# from core.views import index
from core.views import index

app_name = "core"

urlpatterns = [
     path("ecommerce/", index, name="index")
     
]

