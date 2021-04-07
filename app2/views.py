from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def sample2(request):
    return render(request,'sample2.html')
