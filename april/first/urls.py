from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('book', views.book, name="book"),
    path('author', views.author, name="author"),
    path('createauthor', views.createauthor, name="createauthor"),
    path('readauthor/<int:author_id>/', views.readauthor, name="readauthor"),
    path('deleteauthor/<int:author_id>/', views.deleteauthor, name="deleteauthor"),
    path('editauthor/<int:author_id>/', views.editauthor, name="editauthor"),
    path('createbook', views.createbook, name="createbook"),
    path('readbook/<int:book_id>/', views.readbook, name="readbook"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)