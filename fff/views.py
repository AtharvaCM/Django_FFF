from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import CustomUserCreationForm, RegistrationForm
from django.contrib.auth import login
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tokens import account_activation_token
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect

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

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # user.is_active = False so that user can’t login without email confirmation.
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your FreshFromFarm account.'
            message = render_to_string('fff/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            print("domain = " + current_site.domain)
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.content_subtype = 'html'
            email.send()
            template = 'fff/confirm_mail.html'
            context = {}
            return render(request, template, context)
            # return HttpResponse('Please confirm your email address to complete the registration')
        else:
            print(form.errors.as_text())
            return redirect(reverse('register'))
    else:
        form = RegistrationForm()
        context = {'form': form}
        return render(request, 'fff/register.html', context)


@csrf_protect
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        template = 'fff/activate.html'
        context = {}
        return render(request, template, context)
        # return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
