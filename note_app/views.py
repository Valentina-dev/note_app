from django.urls import reverse_lazy
from django.views import generic

from note_app.models import NoteModel
from note_app.forms import NoteForm


class ListNotesView(generic.ListView):
    template_name = 'notes.html'
    queryset = NoteModel.objects.all()
    context_object_name = 'notes'


class NoteDetail(generic.DetailView):
    template_name = 'note.html'
    queryset = NoteModel.objects.all()
    context_object_name = 'note'


class NoteUpdateView(generic.UpdateView):
    form_class = NoteForm
    template_name = 'form.html'
    queryset = NoteModel.objects.all()
    success_url = reverse_lazy("index")


class NoteCreateView(generic.CreateView):
    form_class = NoteForm
    template_name = 'form.html'
    queryset = NoteModel.objects.all()
    success_url = reverse_lazy("index")


class NoteDeleteView(generic.DeleteView):
    queryset = NoteModel.objects.all()
    success_url = reverse_lazy("index")

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)