from django.shortcuts import render
from .forms import LoginForm


def login(request):

    if request.method == 'POST':

        form = LoginForm(request.POST)

        if form.is_valid():

            return render(request, 'greeting/form-data.html', {
                'email': form.cleaned_data['email']
            })

    else:
        form = LoginForm()

    return render(request, 'greeting/index.html', {
        'form': form
    })