from django.shortcuts import render, redirect
from .forms import CreateRfpForm
from donors.models import Donor

def create_rfp(request, donor_id):
    donor = Donor.objects.get(id=donor_id)
    form = CreateRfpForm()

    if request.method == "POST":
        form = CreateRfpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            form.author = request.user
            form.save()
            return redirect('home')

    context = {
        'form': form,
        'donor': donor
    }
    return render(request, 'rfps/add.html', context)
