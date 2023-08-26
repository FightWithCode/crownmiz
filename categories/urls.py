from django.urls import path
from categories import views

app_name = "categories"

urlpatterns = [
    path('create/', views.CreateCategoryView.as_view(), name='category-create'),
    path('', views.AllCategoriesView.as_view(), name='all-categories'),
    path('<int:id>', views.CategoryView.as_view(), name='single-category'),
]
