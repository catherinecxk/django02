from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request, 'home2.html',{"info":"my name is catherine, I like python",})