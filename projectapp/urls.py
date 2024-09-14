from django.urls import path 
from . import views

urlpatterns = [
    
    path("", views.predictor, name="predictor"),
    path("predictLung/", views.predictLung, name="predictLung"),
    path("predictHeart/", views.predictHeart, name="predictHeart"),
    
]
