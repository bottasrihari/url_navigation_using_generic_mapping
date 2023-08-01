from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'name':'srihari','age':24}
    return render(request,'condtions.html',context=d)
 

def data_render(request):
    d={'name':'naidu','age':26}
    return render(request,'data_render.html',context=d)


