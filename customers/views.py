from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Customer

# Create your views here.
def signout(request):
    logout(request)
    return redirect('home')
def show_acccount(request):
    context = {}
    if request.POST and 'register' in request.POST:
        context['register'] = True
        try:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            # create user accounts
            user = User.objects.create_user(
                username = username,
                email = email,
                password = password
            )
            # create customer object
            Customer.objects.create(
                user=user,
                phone=phone,
                address=address
            )
            success_message = "User registersed successfully"
            messages.success(request,success_message)
        except:
            error_message = "Duplicate username or invalid input"
            messages.error(request,error_message)
    if request.POST and 'login' in request.POST:
        context['register'] = False
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Invalid credentials")



    return render(request, 'account.html',context)