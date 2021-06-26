from django.shortcuts import render, redirect
from .models import CustomUser
from .forms import UserForm
from django.views.generic.edit import UpdateView, DeleteView


def create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
        else:
            pass

    return render(request, 'authentication/create.html', {'form': UserForm})


def all_users(request):
    users = CustomUser.get_all()
    return render(request, 'authentication/all.html', context={'users': users})


class update_user(UpdateView):
    model = CustomUser
    template_name = 'authentication/update.html'
    fields = ['first_name', 'middle_name', 'last_name', 'email', 'password']
    success_url = '/users/'


class delete_user(DeleteView):
    model = CustomUser
    template_name = 'authentication/delete.html'
    success_url = '/users/'
