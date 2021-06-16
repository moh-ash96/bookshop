from django.urls import path
from .views import (
    Book_create_view,
    Book_delete_view,
    Book_detail_view,
    Book_list_view,
    Book_update_view,
)

urlpatterns=[
    path("", Book_list_view.as_view(), name="book_list"),
    path("<int:pk>/", Book_detail_view.as_view(), name= "book_detail"),
    path("create/", Book_create_view.as_view(), name="book_create"),
    path("<int:pk>/update/", Book_update_view.as_view(), name="book_update"),
    path("<int:pk>/delete/", Book_delete_view.as_view(), name="book_delete")
]