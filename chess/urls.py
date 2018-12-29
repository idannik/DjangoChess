from django.urls import path
from chess.views import beginner

urlpatterns = [
    path('beginner/', beginner, name='beginner'),

]