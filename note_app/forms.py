from django import forms

from note_app.models import NoteModel


class NoteForm(forms.ModelForm):

    class Meta:
        model = NoteModel
        fields = '__all__'