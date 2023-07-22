from django.shortcuts import render, redirect
from .forms import ApplicationForm
from .models import Application
from django.contrib.auth.models import User
from rfps.models import Rfp

def apply(request, rfp_id):
    rfp = Rfp.objects.get(id=rfp_id)
    user = User.objects.get(id=request.user.id)
    form = ApplicationForm()

    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            Application.objects.create(
                rfp=rfp,
                rep=user.representative,
                concept_note=request.POST["concept_note"]
            )
            # form.save(commit=False)
            # form.rfp = request.POST('rfp')
            # form.rep = user.representative
            # form.save()
            return redirect('home')

    context = {
        'form': form,
        'rfp': rfp
    }
    return render(request, "applications/new.html", context)
