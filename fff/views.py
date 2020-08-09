from django.shortcuts import render

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
