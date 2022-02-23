from curses.ascii import HT
from django.shortcuts import render
from django.http import Http404
# Create your views here.

from .models import Pet

def home(request):
    pets = Pet.objects.all()
    return render(request,'home.html',{'pets':pets,
    })

    #return HttpResponse('<h1>Home Page</h1>')

def pet_detail(request,pet_id):
    try:
        pet = Pet.objects.get(id=pet_id)
    except Pet.DoesNotExist:
        raise Http404('Pet not found')
    return render(request,'pet_detail.html',{'pet':pet})
    #return HttpResponse(f'<h1>pet_detail view with id {pet_id}</h1>')



