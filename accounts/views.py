from django.shortcuts import redirect,render
from django.http import HttpResponse
from .forms import UserForm
from .models import User
from django.contrib import messages

# Create your views here.

def registerUser(request):
    if request.method =='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            # Create the user using the form 
            # password=form.cleaned_data['password']
            # user=form.save(commit=False)
            # user.set_password(password)
            # user.role=User.CUSTOMER
            # user.save()
            
            #create the user using create_user method
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
            user.role=User.CUSTOMER
            user.save()
            messages.success(request,'You account has been registered successfully!')
            return redirect('registerUser')
        else:
            print('Invald forms')
            print(form.errors)
    else:
        form=UserForm()
    context={
        'form':form,
    }
    return render(request, 'accounts/registerUser.html',context)

# from django.shortcuts import render, redirect
# from .forms import UserForm
# from .models import User
# from django.contrib import messages  # For displaying messages

# def registerUser(request):
#     if request.method == 'POST':
#         print(request.POST)
#         form = UserForm(request.POST)
#         if form.is_valid():
#             # Extract the cleaned data
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             username = form.cleaned_data['username']
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']

#             # Check if the user already exists
#             if User.objects.filter(username=username).exists():
#                 messages.error(request, "Username already taken. Please choose a different one.")
#             elif User.objects.filter(email=email).exists():
#                 messages.error(request, "Email already registered. Please use a different email.")
#             else:
#                 # Create the user
#                 user = User.objects.create_user(
#                     first_name=first_name,
#                     last_name=last_name,
#                     username=username,
#                     email=email,
#                     password=password
#                 )
#                 user.role = User.CUSTOMER
#                 user.save()
#                 messages.success(request, "User created successfully.")
#                 print('User is created')
#                 return redirect('registerUser')
#     else:
#         form = UserForm()

#     context = {'form': form}
#     return render(request, 'accounts/registerUser.html', context)



