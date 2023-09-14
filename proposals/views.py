from django.shortcuts import render, redirect
from applications.models import Application

def new_proposal(request, application_id):
    application = Application.objects.get(id=application_id)
    context = {
        
    }
    return render(request, "proposals/new.html", context)
