from django.shortcuts import render

# Create your views here.

def learnit(request):
    return render(request, 'learnit.html')
