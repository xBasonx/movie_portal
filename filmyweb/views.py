from django.shortcuts import render
from django.http import HttpResponse

def test_response(request):
    return HttpResponse("<h1>To jest nasz pierwszy test</h1>")