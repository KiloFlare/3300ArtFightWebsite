from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
    path('', views.index, name='index'),
    path('recent/', views.recent, name='recent'),
    path('individualArt/<int:pk>', views.individualArtView.as_view(), name='individualArt-detail'),
    path('art/upload/', views.uploadArtForm, name='upload-art-form'),
    path('art/<int:id>/update/', views.updateIndividualArtForm, name='update-art-form'),
    path('art/<int:id>/delete/', views.deleteIndividualArtForm, name='delete-art-form'),


]
