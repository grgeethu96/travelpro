from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, Team


def demo(request):
    obj = Place.objects.all()
    obj1 = Team.objects.all()
    return render(request, "index.html", {'result': obj, 'team': obj1})


# def addition(request):
#     num_1 = int(request.GET['num1'])
#     num_2 = int(request.GET['num2'])
#     result = num_1 + num_2
#     return render(request, "about.html",{'result': result})


# def contact(request):
#     return HttpResponse("Hai Ila, Iam contact")
