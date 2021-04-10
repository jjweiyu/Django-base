from django.urls import path
from test_01.views import index
urlpatterns = [
    path('index/', index)
]