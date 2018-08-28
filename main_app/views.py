from django.shortcuts import render, render_to_response

# Create your views here.


def main_view(request):
    name = 'Kirill'
    return render_to_response('about.html', {'name': name})


def contact(request):
    return render_to_response('contact.html')


def experience(request):
    return render_to_response('experience.html')