from django.urls import path
from . import views
from .views import (
    book_list_view,
    LibraryDetails_view,
    admin_view,
    librarian_view,
    member_view,
    add_book,
    edit_book,
    delete_book,
    RegisterView,
    CustomLoginView,
    CustomLogoutView
)

urlpatterns = [
    path('', book_list_view, name='home'),  # عرض قائمة الكتب كصفحة رئيسية
    path('library/<int:pk>/', LibraryDetails_view.as_view(), name='library_detail'),  # عرض تفاصيل المكتبة


    path('login/', CustomLoginView.as_view(template_name="authentication/login.html"), name='login'),
    path('logout/', CustomLogoutView.as_view(template_name="authentication/logout.html"), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),


    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),


    path('books/add_book/', add_book, name='add_book'),
    path('books/edit_book/<int:book_id>/', edit_book, name='edit_book'),
    path('books/delete_book/<int:book_id>/', delete_book, name='delete_book'),
]
