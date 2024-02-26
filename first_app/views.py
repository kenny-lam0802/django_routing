from django.shortcuts import render, HttpResponse

# Create your views here.
def first_view(request):
    return HttpResponse("This is first_app and FIRST VIEW!")

def second_view(request):
    return HttpResponse("This is the first_app SECOND VIEW!")

def one_method(request):
    return HttpResponse("Fast cars!")

def another_method(request, my_val):
    return HttpResponse("You've entered a NUMBER in the URL!")

def name_method(request, name):
    return HttpResponse("You've entered a NAME!")

def id_color(request, id, color):
    return HttpResponse("You've entered a NUMBER and NAME")