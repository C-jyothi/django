from django.shortcuts import render

def employees(request):
    employee_list = [
        {
            "name": "Anu",
            "job_title": "Software Developer",
            "salary": 50000,
            "full_time": True
        },
        {
            "name": "Rahul",
            "job_title": "Designer",
            "salary": 40000,
            "full_time": False
        },
        {
            "name": "Meera",
            "job_title": "Project Manager",
            "salary": 60000,
            "full_time": True
        }
    ]

    return render(request, "employees.html", {
        "employees": employee_list
    })
