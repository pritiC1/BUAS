from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .models import CustomUser 
from .forms import UserRegistrationForm
from .forms import LoginForm
from django.contrib.auth import logout
from django.http import JsonResponse
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings




def index(request):
    return render(request, 'index.html') 

def register(request):
    if request.method == 'POST':
        user_first_name = request.POST.get('first_name')
        user_middle_name = request.POST.get('middle_name')
        user_last_name = request.POST.get('last_name')
        user_date_of_birth = request.POST.get('date_of_birth')
        user_gender = request.POST.get('gender')
        user_email = request.POST.get('email')
        user_password = request.POST.get('password')
        user_confirm_password = request.POST.get('confirm_password')
        user_contact_number = request.POST.get('contact')

        # Check if passwords match
        if user_password != user_confirm_password:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'register.html')

        # Create the user object (assuming you're using a custom user model)
        user = CustomUser(
            username=user_email,  # or another unique field like a username
            first_name=user_first_name,
            middle_name=user_middle_name,
            last_name=user_last_name,
            date_of_birth=user_date_of_birth,
            gender=user_gender,
            contact_number=user_contact_number,
            email=user_email,
            is_active=False
                
        )
        user.generate_otp()
        user.set_password(user_password) 
        user.generate_otp()
        user.save()  

        send_mail(
            'Email Verification OTP',
            f'Your OTP for verification is: {user.otp}',
            settings.DEFAULT_FROM_EMAIL,
            [user_email],
            fail_silently=False,
        )
        
        request.session['email'] = user_email
        messages.success(request, 'Registration successful! Check your email for OTP verification.')
        return redirect('verify_otp')  

    return render(request, 'register.html')
       
def login_view(request):
    # Initialize the form
    form = AuthenticationForm()

    if request.method == 'POST':
        # Populate the form with the POST data
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():  # Check if the form is valid
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                return JsonResponse({'success': True})  # Return success response after login
            else:
                return JsonResponse({'success': False, 'message': 'Invalid credentials'})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid form data'})
        
    
    return render(request, 'login.html', {'form': form})
def dashboard(request):
    return render(request, 'dashboard.html')
def logout_view(request):
    logout(request)
    return redirect('login')
def forgot_password(request):
    if request.method == 'POST':
        # Handle password reset logic here
        pass  # Add your actual password reset logic
    return render(request, 'forgot_password.html')

class CustomPasswordResetView(PasswordResetView):
    template_name = 'forgot_password.html'
    success_url = reverse_lazy('password_reset_done')
    email_template_name = 'password_reset_email.html'
    form_class = PasswordResetForm


def verify_otp(request):
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        email = request.session.get('email')

        try:
            # Fetch the user using email stored in session
            user = CustomUser.objects.get(email=email)

            # Check if entered OTP matches
            if str(user.otp) == entered_otp:
                user.is_active = True  # Activate the user upon successful OTP verification
                user.otp = None  # Clear OTP after successful verification
                user.save()

                messages.success(request, 'Your account has been verified. You can now log in.')
                return redirect('login')
            else:
                messages.error(request, 'Invalid OTP. Please try again.')

        except CustomUser.DoesNotExist:
            messages.error(request, 'User not found. Please register again.')
            return redirect('register')

    return render(request, 'verify_otp.html')
