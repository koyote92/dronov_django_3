from django.shortcuts import render
from django.http import HttpResponse

from .models import Bb


def index(request):
    template = 'bboard/index.html'
    bbs = Bb.objects.all()
    context = {'bbs': bbs}
    return render(request, template, context)
