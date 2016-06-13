from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def inicio(request):
    template = loader.get_template('index.html')
    title = "Registrese"
    context = {
        'title': title
    }
    return HttpResponse(template.render(context, request))
