from django.shortcuts import render

def home_page(request):
    return render(request, 'home.html')

def beginner(request):
    return render(request, 'chess.html')
