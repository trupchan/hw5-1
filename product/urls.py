from django.urls import path
from .views import (
    CategoryListCreateView, CategoryRetrieveUpdateDestroyView,
    ProductListCreateView, ProductRetrieveUpdateDestroyView,
    ReviewListCreateView, ReviewRetrieveUpdateDestroyView,
)

urlpatterns = [
    
    path('categories/', CategoryListCreateView.as_view()),                 
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view()),  

    
    path('products/', ProductListCreateView.as_view()),                    #
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view()),   
    

    path('reviews/', ReviewListCreateView.as_view()),                      
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDestroyView.as_view()),      
]


