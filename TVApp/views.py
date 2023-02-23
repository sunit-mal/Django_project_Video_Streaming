from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

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
    if request.user.is_authenticated:
        return render(request, 'ghostStory.html')
    else:
        return HttpResponseRedirect('/login/')

def about(request):
    return render(request, 'about.html')

def search(request):
    if request != 'GET':
        name = request.GET['search']
        name = name.upper()
        if (name == '777' or name == 'CHARLIE'):
            return HttpResponseRedirect('/Charlie/')

        elif (name == 'CHUP'):
            return HttpResponseRedirect('/chup/')

        elif (name == 'FREDDY'):
            return HttpResponseRedirect('/freddy/')

        elif (name == 'GHOST STORY'or name == 'GHOSTSTORY'):
            return HttpResponseRedirect('/ghostStory/')

        elif (name == 'GOODBYE'or name == 'GOOD BYE'):
            return HttpResponseRedirect('/GoodByeMovie/')

        else:
            return HttpResponseRedirect('/')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return render(request, 'login.html')
        else:
            return render(request, 'login.html')
    else:
        return HttpResponseRedirect('/')

def uesr_signup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        user = request.POST['uname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        email = request.POST['email']
        if(pass1 == pass2):
            user_exist = User.objects.filter(username=user).exists()
            if user_exist :
                messages.success(request, 'This username already exists. Please use a different one.')
                return HttpResponseRedirect("/signup/")
            else:
                myuser = User.objects.create_user(user,email,pass1)
                myuser.first_name = fname
                myuser.last_name = lname
                myuser.save()

                # for login after signup 
                user = authenticate(request, username=user, password=pass1)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/')

        else:
            messages.success(request, "Password Not match. Re-enter password correctly.")
            return HttpResponseRedirect("/signup/")
    else:
        return render(request, 'sign_up.html')

def dashboard(request):
    if request.user.is_authenticated:
        user = request.user
        full_name = user.get_full_name()
        return render(request, 'index.html',{'full_name':full_name})
    else:
        return render(request, 'index.html',{'full_name':"User"})
    
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')