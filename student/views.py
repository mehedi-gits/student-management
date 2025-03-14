from django.shortcuts import render

# Create your views here.

def homepage(request):

    student = [
        {
        'Name': 'Name1',
        'Email': 'Email1',
        'Phone': 'Phone1',
        'Course': 'Course1'
        },
        {
        'Name': 'Name2',
        'Email': 'Email2',
        'Phone': 'Phone2',
        'Course': 'Course2'
        },
        {
        'Name': 'Name3',
        'Email': 'Email3',
        'Phone': 'Phone3',
        'Course': 'Course3'
        }
    ]

    context = {
        'student': student
        }

    return render(request, 'student/home.html', context)