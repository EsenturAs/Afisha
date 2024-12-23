from django.urls import path
from . import views

urlpatterns = [
    path('directors/', views.director_list_view),
    path('movies/', views.movie_list_view),
    path('movies/reviews/', views.reviews_for_movie_list_view),
    path('reviews/', views.review_list_view),
    path('directors/<int:id>/', views.director_detail_view),
    path('movies/<int:id>/', views.movie_detail_view),
    path('reviews/<int:id>/', views.review_detail_view),
]