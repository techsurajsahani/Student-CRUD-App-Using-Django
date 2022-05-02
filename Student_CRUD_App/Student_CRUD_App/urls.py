from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from student import views

urlpatterns = [
    path('admin/', admin.site.urls),
       
 # Admin URL's
 path('', views.home, name='home'),
 
 path('search/', views.search, name='search'),

 
 path('create/', views.StudentCreateView.as_view(), name='create'),
 path('list', views.StudentListView.as_view(), name='list'),
 path('view/<int:pk>', views.StudentDetailView.as_view(), name='view'),
 path('update/<int:pk>', views.StudentUpdateView.as_view(), name='update'),
 path('delete/<int:pk>', views.StudentDeleteView.as_view(), name='delete'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
