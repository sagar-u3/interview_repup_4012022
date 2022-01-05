from django.urls import path
from api.api import BoardViewset

urlpatterns = [
    path('boards/', BoardViewset.as_view({'post': 'create'})),
    path('boards/<int:pk>', BoardViewset.as_view({'put': 'update'}))
]
