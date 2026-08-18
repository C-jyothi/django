from django.shortcuts import render
from .forms import MovieForm
from .models import Movie

def greeting(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)

        if form.is_valid():
            movie = Movie()
            movie.movie_name = form.cleaned_data['movie_name']
            movie.release_date = form.cleaned_data['release_date']
            movie.save()

            return render(request, 'form-data.html', {
                'message': 'Movie data saved to db'
            })

    else:
        form = MovieForm()

    return render(request, 'index.html', {'form': form})