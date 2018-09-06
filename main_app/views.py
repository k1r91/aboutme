from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.shortcuts import render, render_to_response, Http404
from .models import Person, Work, Education, Organization

# Create your views here.


def organization(request, slug):
    try:
        organization = Organization.objects.get(slug=slug)
    except ObjectDoesNotExist:
        raise Http404
    person = Person.objects.all()[0]
    return render_to_response('organization.html', {'organization': organization, 'person': person})


def main_view(request):
    person = Person.objects.all()[0]
    return render_to_response('about.html', {'page': 'about', 'person': person})


def contact(request):
    person = Person.objects.all()[0]
    return render_to_response('contact.html', {'page': 'contact', 'person': person})


def experience(request):
    person = Person.objects.all()[0]
    works = Work.objects.all()
    return render_to_response('experience.html', {'page': 'experience', 'person': person, 'works': works})


def education(request):
    person = Person.objects.all()[0]
    educations = Education.objects.all()
    return render_to_response('education.html', {'page': 'education', 'person': person, 'educations': educations})


def portfolio(request):
    person = Person.objects.all()[0]
    return render_to_response('portfolio.html', {'page': 'portfolio', 'person': person})


def services(request):
    person = Person.objects.all()[0]
    return render_to_response('services.html', {'page': 'services', 'person': person})


def skills(request):
    person = Person.objects.all()[0]
    return render_to_response('skills.html', {'page': 'skills', 'person': person})


def testimonials(request):
    person = Person.objects.all()[0]
    return render_to_response('testimonials.html', {'page': 'testimonials', 'person': person})