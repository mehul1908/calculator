from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
# Create your views here.

def error_404_view(request,exception):
    return render(request,'404.html')

def index(request):
    return render(request , 'index.html')

def submitquery(request):
    q=request.GET['query']
    try:
        ans = eval(q)
        mydict={
            "q":q+":",
            "ans":ans,
            "success":True
        }
        return render(request,'index.html' , context=mydict)
    except:
        mydict={
            "error":True
        }
        return render(request,'index.html' , context=mydict)

