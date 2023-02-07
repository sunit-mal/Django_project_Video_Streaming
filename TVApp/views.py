from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .forms import SignUpForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

def homepage(request):
    return render(request, 'index.html')

def goodbye(request):
    # return render(request, 'GoodByeMovie.html')
    if request.user.is_authenticated:
        return render(request, 'GoodByeMovie.html')
    else:
        return HttpResponseRedirect('/login/')

def charlie(request):
    if request.user.is_authenticated:
        return render(request, 'Charlie.html')
    else:
        return HttpResponseRedirect('/login/')

def chup(request):
    # return render(request, 'chup.html')
    if request.user.is_authenticated:
        return render(request, 'Chup.html')
    else:
        return HttpResponseRedirect('/login/')

def freddy(request):
    # return render(request, 'freddy.html')
    if request.user.is_authenticated:
        return render(request, 'freddy.html')
    else:
        return HttpResponseRedirect('/login/')

def ghoststory(request):
    # return render(request, 'ghostStory.html')
    if request.user.is_authenticated:
        return render(request, 'ghostStory.html')
    else:
        return HttpResponseRedirect('/login/')

def about(request):
    return render(request, 'about.html')

def search(request):
    if request == 'GET':
        name = request.GET.get('search')
        return HttpResponse(name)
    
def uesr_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Registered Successfull')
            form.save()
            return HttpResponseRedirect('/login/')
    else:
        form = SignUpForm()

    return render(request, 'sign_up.html',{'form': form})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    # messages.success(request, 'Logged in successfully')
                    return HttpResponseRedirect('/')
        else:
            form = LoginForm()
        return render(request, 'login.html', {'form': form})
    else:
        return HttpResponseRedirect('/')

def dashboard(request):
    if request.user.is_authenticated:
     user = request.user
     full_name = user.get_full_name()
     return render(request, 'index.html',{'full_name':full_name})
    else:
      return HttpResponseRedirect('/')
    
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')