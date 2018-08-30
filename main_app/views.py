from django.shortcuts import render, render_to_response

# Create your views here.


def main_view(request):
    name = 'Kirill'
    return render_to_response('about.html', {'page': 'about'})


def contact(request):
    return render_to_response('contact.html', {'page': 'contact'})


def experience(request):
    return render_to_response('experience.html', {'page': 'experience'})


def education(request):
    return render_to_response('education.html', {'page': 'education'})


def portfolio(request):
    return render_to_response('portfolio.html', {'page': 'portfolio'})


def services(request):
    return render_to_response('services.html', {'page': 'services'})


def skills(request):
    return render_to_response('skills.html', {'page': 'skills'})


def testimonials(request):
    return render_to_response('testimonials.html', {'page': 'testimonials'})