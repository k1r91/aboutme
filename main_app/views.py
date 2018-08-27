from django.shortcuts import render, render_to_response

# Create your views here.


def main_view(request):
    name = 'Kirill'
    return render_to_response('index.html', {'name': name})