from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Author
from .forms import AuthorForm
from django.views.generic import UpdateView, DeleteView


def author_list(request):
    authors = Author.objects.all()
    return render(request, "author/author_list.html", {'authors': authors})


class AuthorUpdateView(UpdateView):
    model = Author
    template_name = 'author/update.html'
    fields = ['name', 'surname', 'patronymic']


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'author/delete.html'
    success_url = '/author'


def create(request):
    error = ''
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/author/list')
        else:
            error = 'data is not valid'

    form = AuthorForm()
    data = {'form': form, 'error': error}
    return render(request, 'author/create.html', data)


