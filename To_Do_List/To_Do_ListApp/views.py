from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        "name" : "Ethan"
    }
    return render(request, "To_Do_ListApp/home.html", context)