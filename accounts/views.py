from django.contrib import messages, auth
from django.shortcuts import render, redirect
from contacts.models import Contact
from django.contrib.auth.models import User

from contacts.views import contact

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request,user)
            messages.success(request, 'You are now Logged In')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect ('login')

    else:
        return render(request, 'accounts/login.html')


def logout(request):
        auth.logout(request)
        messages.success(request, 'You are now Logged Out')
        return redirect ('home') 

def register(request):
    if request.method == 'POST':
        #Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if password match
        if password == password2:
        
            # Check if Username does not exist
            if User.objects.filter(username = username).exists():
                messages.error(request, 'Username is already taken')
                return redirect('register')
            else:
                # Check if Email does not exist
                if User.objects.filter(email = email).exists():
                    messages.error(request, 'Email is already exist')
                    return redirect('register')
                else:
                    # Login Successful
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    messages.success(request,'Congratulations, you are now Logged In')
                    return redirect ('login')
        else:
            messages.error(request, 'Password do not match')
            return redirect('register')

    else:
        return render(request, 'accounts/register.html')

def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date'). filter(user_id=request.user.id)
    context = {
        'contacts': user_contacts
    }
    return render(request, 'accounts/dashboard.html', context)