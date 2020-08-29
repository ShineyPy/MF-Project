from django.contrib import admin
from django.urls import path
from MF import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',views.Student_view)
    path('',views.index_v),
    path('addmovie/',views.add_movie),
    path('listmovie/',views.list_movie),
]
