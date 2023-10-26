from django.urls import path
from note_app.views import ListNotesView, NoteDetail, NoteDeleteView, NoteUpdateView, NoteCreateView

urlpatterns = [
    path('', ListNotesView.as_view(), name="index"),
    path('create/', NoteCreateView.as_view(), name="create-form"),
    path('<pk>/', NoteDetail.as_view(), name="detail"),
    path('delete/<pk>/', NoteDeleteView.as_view(), name="delete"),
    path('update/<pk>/', NoteUpdateView.as_view(), name="update"),
]