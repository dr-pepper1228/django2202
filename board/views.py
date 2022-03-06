import re
from django.shortcuts import render,redirect
from .models import Board,Reply
from django.utils import timezone
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    kw=request.GET.get("kw","")
    cate=request.GET.get("cate","")
    if kw:
        if cate=="sub":
            b=Board.objects.filter(subject__contains=kw)
        elif cate=="wri":
            try:
                from acc.models import User
                u=User.objects.get(username=kw)
                b=Board.objects.filter(writer=u)
            except:
                b=Board.objects.none()
    else:
        b=Board.objects.all()
    b=b.order_by('-pubdate')
    page=request.GET.get("page",1)
    pag=Paginator(b,10)
    obj=pag.get_page(page)
    
    context={
        'bset':obj,
        'kw':kw,
        'cate':cate
    }
    return render(request,"board/index.html",context)

def create(request):
    if request.method=="POST":
        s=request.POST.get("sub")
        c=request.POST.get("com")
        if s and c:
            Board(subject=s,content=c,writer=request.user,pubdate=timezone.now()).save()
            return redirect("board:index")
    return render(request,"board/create.html")

def detail(request,bpk):
    
    d=Board.objects.get(id=bpk)
    r=d.reply_set.all()
    context={
        'd':d,
        'rset':r
    }
    return render(request,"board/detail.html",context)

def delete(request,bpk):
    d=Board.objects.get(id=bpk)
    if request.user == d.writer:
        d.delete()
    else:
        pass # 내일 할 거
    return redirect("board:index")

def update(request,bpk):
    d=Board.objects.get(id=bpk)
    if request.user != d.writer:
        return redirect("board:index")
    if request.method=="POST":
        s=request.POST.get("sub")
        c=request.POST.get("com")
        d.subject,d.content=s,c
        d.save()
        return redirect("board:detail",bpk)
    context={
        'd':d
    }
    return render(request,"board/update.html",context)

def creply(request,bpk):
    c=Board.objects.get(id=bpk)
    r=request.POST.get("com")
    if c:
        Reply(board=c,replyer=request.user,comment=r).save()
        return redirect("board:detail",bpk)

def dreply(request,bpk,rpk):
    re=Reply.objects.get(id=rpk)
    if request.user == re.replyer:
        re.delete()
    return redirect("board:detail",bpk)

def likey(request,bpk):
    b=Board.objects.get(id=bpk)
    b.likey.add(request.user)
    return redirect("board:detail",bpk)

def cancel(request,bpk):
    b=Board.objects.get(id=bpk)
    b.likey.remove(request.user)
    return redirect("board:detail",bpk)