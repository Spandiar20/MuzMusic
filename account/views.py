from django.shortcuts import render,redirect
from .forms import SignUpForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


def register_user(request):
    form=SignUpForm()
    if request.method == 'POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.first_name=form['first_name'].value().capitalize()
            user.last_name=form['last_name'].value().capitalize()
            user.save()
            first_name=form.cleaned_data['first_name']
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
           
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,(f'Welcome to MuzMusic dear {first_name}'))
            redirect('')
    return render(request,'account/register.html',{
        'form':form
    })
