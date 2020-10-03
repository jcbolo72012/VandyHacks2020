from django.shortcuts import render
from .models import Member, TempMember
from .forms import MemberForm
from django.contrib import messages
from django.core import validators


# Create your views here.
def home(request):
    all_members = Member.objects.all
    return render(request, 'home.html', {'all':all_members})

def join(request):
    if request.method == "POST":
        
        form = MemberForm(request.POST or None)
        # form1 = form.save(commit=False)
        # form1.credits = 0
        # form1.age = 0
        # form1.cname = ""
        if form.is_valid():
            form.save()
        messages.success(request, ("Your form has been submitted!!"))
        m = Member(fname = form['fname'], lname = form['lname'], email=form['email'], passwd=form['passwd'], cname="", age = 0, credits=0)
        m.save(force_insert=True)
        return render(request, 'home.html', {})
    else:
        return render(request, 'join.html', {})