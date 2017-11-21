from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PCForm, ReservationForm
from .models import Pc
from .models import Floor


# Create your views here.
# def hello(request):
#	return render(request, "blog/template/hello.html", {})

def hello(request):
    pcform = PCForm(request.POST, request.POST)
    # pc = Pc(PCForm())
    # pc.save()

    if pcform.is_valid():
        pc = Pc()
        pc.floor_num = Floor.objects.get(pk=pcform.cleaned_data["Floor_Num"])
        pc.pc_num = pcform.cleaned_data["PC_Num"]
        pc.save()
        return render(request, 'book.html', {})

    return render(request, 'hello.html', {'form': pcform})


def index(request):
    return render(request, 'index.html', {})


def book(request):
    mychoice = Floor.objects.all().values_list('floor_num', 'floor_name')
    reservation = ReservationForm(choice=mychoice)
    return render(request, 'book.html', {'form': reservation})
