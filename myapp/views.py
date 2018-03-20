from django.shortcuts import render,redirect,HttpResponse
from . models import Text
# Create your views here.


def index(request):
    if request.method=='GET':
        return render(request, 'index.html')
    else:
        t = request.POST.get('tt')
        print(t)
        ttt = Text()
        s = ttt.create(t)
        s.save()
        return redirect('/post1/'+str())

def post1(req,p):
    l = Text.objects.filter(id=p)

    print(l)
    return render(req,'post1.html',{'l':l})