from django.shortcuts import render, redirect
from .forms import LoginForm, SignUpForm
from django.contrib.auth import authenticate,  login as auth_login, logout as auth_logout
from django.views.decorators.csrf import csrf_exempt
from .models import User
from django.contrib import messages 

@csrf_exempt
def signup(request):
    msg = ""
    field_errors = {}
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect("login_view")
        else:
            # Process specific error messages
            for field, errors in form.errors.items():
                if field == "password2":
                    if "The two password fields didn't match." in str(errors):
                        field_errors["password2"] = "Passwords do not match."
                    else:
                        field_errors["password2"] = "Password is too weak. Make sure it meets all requirements."
                elif field == "username":
                    if "already exists" in str(errors):
                        field_errors["username"] = "This username is already taken."
                    else:
                        field_errors["username"] = str(errors[0])
                elif field == "email":
                    field_errors["email"] = str(errors[0])
                else:
                    field_errors[field] = str(errors[0])
            if not field_errors:
                msg = "There was an error creating your account. Please check your information and try again."
    else:
        form = SignUpForm()
        
    context = {
        'form': form, 
        'msg': msg,
        'field_errors': field_errors
    }
    return render(request, "signup.html", context)


@csrf_exempt
def login(request):
    msg = None
    error_type = None
    form = LoginForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            
            if user is not None:
                auth_login(request, user)
                return redirect('dashboard')
            else:
                msg = "Invalid username or password"
                error_type = "credentials"
        else:
            msg = "Please fill in all fields correctly"
            error_type = "form"
            
    return render(request, "login.html", {
        'form': form, 
        'msg': msg,
        'error_type': error_type
    })

def logout(request):
    auth_logout(request)
    return redirect("login_view")

def dashboard(request):
    if (request.user.is_authenticated):
        user = User.objects.get(username=request.user)
        if(user.is_coordinator):
            return render(request, "coordinatorDash.html", {"user": user, 'created': user.events_created.split(), 'length': len(user.events_created.split()), 'range': range(len(user.events_created.split()))})
        else:
            return render(request, "studentDash.html", {"user": user, 'participated': user.events_participated.split(), 'length': len(user.events_participated.split()), 'range': range(len(user.events_participated.split()))})
    else:
        return redirect('login_view')


