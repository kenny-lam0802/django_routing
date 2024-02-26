from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

# Create your views here.
def first_view(request):
    return HttpResponse("This is the second_app FIRST VIEW!")

def second_view(request):
    return HttpResponse("This is the second_app SECOND VIEW")

def root_method(request):
    return HttpResponse("This is your root route!")

def another_method(request):
    return redirect("/second-app/redirected_route")

def redirected_method(request):
    return JsonResponse({"response": "JSON response from the redirected_method", "status": True})

