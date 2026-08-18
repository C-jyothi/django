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
def result(request, name):

    students = {
        'Rahul': 85,
        'Anu': 92,
        'Arun': 76,
    }

    marks = students.get(name)

    return render(request, 'students/result.html', {
        'name': name,
        'marks': marks
    })