from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .forms import UserForm, middleManAvatar
from .models import UserAvatar


# Create your views here.
def index(request):
	return render(request, 'games/index.html')

def loginpage(request):
	return render(request, 'games/login.html')

def signup(request):
	form = UserForm(request.POST or None)
	avatar_form = middleManAvatar(request.POST or None, request.FILES or None)
	if form.is_valid():
		userN = form.save(commit=False)
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		userN.set_password(password)
		userN.save()

		avatar_profile = UserAvatar()
		avatar_profile.username = username
		avatar_profile.avatar = request.FILES['avatar']
		avatar_profile.save()
		userN = authenticate(username=username, password=password)
		


		# if user is not None:
  #           if user.is_active:
  #               login(request, user)
  #               albums = Album.objects.filter(user=request.user)
  #               return render(request, 'music/index.html', {'albums': albums})



		if userN is not None:
			if userN.is_active:
				login(request, userN)
				# albums = Album.objects.filter(user=request.user)
				return render(request, 'games/index.html') #, {'albums': albums})


	avatar_form = middleManAvatar()
	context = {
	    "form": form,
	    "avatar_form" : avatar_form,
	}
	return render(request, 'games/signup.html', context)

def myAccount(request):
	# if request.user.is_authenticated():
	# 	user = request.user
	# 	pic = UserAvatar.objects.filter(user=request.user)
	return render(request, 'games/myAccount.html')#, {'pic':pic})

def reward(request):
	return render(request, 'games/reward.html')

def purchased(request):
	return render(request, 'games/purchased.html')