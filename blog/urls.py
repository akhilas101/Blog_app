from django.urls import path,include
from. import views

urlpatterns = [
    path('post/',views.addPost,name="post"),
    path('View/',views.viewAll,name="View"),
    path('ViewMy/',views.viewMyPost,name="ViewMy"),
]
