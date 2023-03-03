from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method== 'POST':
        fname=request.POST['firstName']
        lname = request.POST['lastname']
        email = request.POST['email']
        uname = request.POST['uname']
        passw = request.POST['pass']
        cpassw = request.POST['cpass']

        if passw==cpassw:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"username is already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email is already taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=uname,password=passw,first_name=fname,last_name=lname,email=email,)
                user.save()
                print("user created")
        else:
            #print("password mismatching")
            messages.info(request,"password mismatch")
            return redirect('register')
        return redirect('/')
    return render (request,'reg.html')

def login(request):
    if request.method=='POST':
        username=request.POST['uname']
        password=request.POST['pass']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')