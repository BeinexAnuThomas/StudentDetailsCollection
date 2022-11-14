from django.urls import path
from studentapp import views

urlpatterns = [
    path('', views.home,name='home'),
    path('register',views.register,name='register'),
    path('viewlist',views.viewlist,name='viewlist'),
    path('updatelist/<str:pk>/',views.updatelist,name='updatelist'),
    path('deletelist/<str:pk>/',views.deletelist,name='deletelist'),
]
