from django.shortcuts import render


def index(request):
    template_name = 'freshfromfarm/index.html'
    context = {}
    return render(request, template_name, context)


def about(request):
    template_name = 'freshfromfarm/about.html'
    context = {}
    return render(request, template_name, context)


def contact(request):
    template_name = 'freshfromfarm/contact.html'
    context = {}
    return render(request, template_name, context)
