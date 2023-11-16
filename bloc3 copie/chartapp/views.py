from django.shortcuts import render

# Create your views here.

def index(request):
    data = "Current data"

    context={
    "study": data
    }

    return render(request, 'chartapp/index.html', context)