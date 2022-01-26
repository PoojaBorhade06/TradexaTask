from .import views
from django.urls import path
urlpatterns=[
    path('tv/',views.testView,name='home'),
    path('av/',views.addPostView,name='addorder'),
    path('sv/',views.showPostView,name='showorder'),

]