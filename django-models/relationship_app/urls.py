from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView  # Import from Django's built-in views
from django.contrib.auth.registration.views import RegisterView  # Import from registration app

urlpatterns = [
    path('', views.book_list_view, name='home'),  # Single path for home view

    # Authentication URLs (using Django's built-in views)
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(template_name='registration/register.html'), name='register'),  # Specify template location

    # Role-based access control paths (replace with actual views or permissions)
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),

    # Book management URLs
    path('books/add_book/', views.add_book, name='add_book'),
    path('books/edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('books/delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
]