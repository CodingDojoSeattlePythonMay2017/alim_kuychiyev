# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def index(request):

    return render(request, 'turtles_app/index.html')

def allninjas(request):
    return render(request, 'turtles_app/show.html')

def show(request,turtles):

    if turtles == 'blue':
        color = 'static/turtles_app/Ninjas/leonardo.jpg'
    elif turtles == 'orange':
        color = 'static/turtles_app/Ninjas/michelangelo.jpg'
    elif turtles == 'red':
        color = 'static/turtles_app/Ninjas/raphael.jpg'
    elif turtles == 'purple':
        color = 'static/turtles_app/Ninjas/donatello.jpg'
    else:
        color = 'static/turtles_app/Ninjas/notapril.jpg'


    showninjas = {
                    'showthem': color
                }

    return render(request, 'turtles_app/turtles.html', showninjas)
