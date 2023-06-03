from django.urls import path, include
import api.views as api_views

urlpatterns = [
    path('getNotes/', api_views.getNotes, name='getNotes'),
    path('getOneNote/<int:serial>', api_views.getOneNote, name='getOneNote'),
    path('addNotes/', api_views.addNotes, name='addNotes'),
    path('updateNote/<str:serial>', api_views.updateNote, name='updateNote'),
    path('deleteNote/<str:serial>', api_views.deleteNote, name='deleteNote'),

]