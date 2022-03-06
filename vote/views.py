from django.shortcuts import render,redirect
from .models import Choice, Topic
# Create your views here.

def index(request):
    t=Topic.objects.all()
    context={
        'tset':t
    }
    return render(request,"vote/index.html",context)

def detail(request,bpk):
    d=Topic.objects.get(id=bpk)
    c=d.choice_set.all()
    context={
        'd':d,
        'cset':c
    }
    return render(request,"vote/detail.html",context)

def vote(request,bpk):
    t=Topic.objects.get(id=bpk)
    if not request.user in t.voter.all():
        t.voter.add(request.user)
        cpk=request.POST.get("ch")
        c=Choice.objects.get(id=cpk)
        c.chnum +=1
        c.save()
    return redirect("vote:detail",bpk)