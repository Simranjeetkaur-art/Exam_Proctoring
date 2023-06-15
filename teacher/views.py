from django.shortcuts import render

def t_index(request):
    return render(request, "teacher.html")
