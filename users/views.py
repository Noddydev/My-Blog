from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
	if request.method=='POST':
		form_obj=UserCreationForm(request.POST)
		if form_obj.is_valid():
			form_obj.save()
			un=form_obj.cleaned_data.get('username')
			messages.success(request,f'Congratulation {un},your account has been created successfully')
			return redirect('login')
	else:
		form_obj=UserCreationForm()
		return render(request,'users/register.html',{'form':form_obj})

@login_required
def profile(request):
	return render(request,'users/profile.html')