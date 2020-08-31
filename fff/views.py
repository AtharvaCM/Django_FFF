from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import CustomUserCreationForm, RegistrationForm
from django.contrib.auth import login

# Create your views here.


def index(request):
    template_name = 'fff/index.html'
    context = {}
    return render(request, template_name, context)


def about(request):
    template_name = 'fff/about.html'
    context = {}
    return render(request, template_name, context)


def contact(request):
    template_name = 'fff/contact.html'
    context = {}
    return render(request, template_name, context)


def services(request):
    template_name = 'fff/services.html'
    context = {}
    return render(request, template_name, context)


# def register(request):
#     template_name = 'fff/register.html'
#     if request.method == "GET":
#         print("inside  if")
#         return render(
#             request, template_name,
#             {"form": CustomUserCreationForm}
#         )
#     elif request.method == "POST":
#         form = CustomUserCreationForm(request.POST)
#         print("Inside")
#         if form.is_valid():  # this condition is not getting true
#             user = form.save()
#             login(request, user)
#             # form is not saving
#             return redirect(reverse('freshfromfarm-home'))
#         else:
#             return redirect(reverse('freshfromfarm-services'))


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('freshfromfarm-home'))
        else:
            print(form.errors.as_text())
            return redirect(reverse('register'))
    else:
        form = RegistrationForm()
        context = {'form': form}
        return render(request, 'fff/register.html', context)
