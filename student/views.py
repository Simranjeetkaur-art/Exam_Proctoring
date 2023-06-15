from django.shortcuts import render

def st_index(request):
    return render(request, "student.html")
