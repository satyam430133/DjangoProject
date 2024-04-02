from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
def home(request):
    # return HttpResponse("HEllo THis o9os not")
    return render(request,'index.html')