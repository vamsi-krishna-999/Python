from django.urls import path
from .views import *

urlpatterns = [
    path('',booklist,name='get books'),
    path('add/',postbook,name='create book'),
    path('update/<int:id>/',updatebook,name='update book'),
    path('delete/<int:id>/',deletebook,name='delete book'),
]
