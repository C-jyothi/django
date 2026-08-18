from django.shortcuts import render

def home(request):

    students = [
        {'name': 'Rahul', 'marks': 85},
        {'name': 'Anu', 'marks': 92},
        {'name': 'Arun', 'marks': 76},
    ]

    return render(request, 'students/home.html', {
        'students': students
    })