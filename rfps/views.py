from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CreateRfpForm
from donors.models import Donor

@login_required()
def create_rfp(request, donor_id):
    if not request.user.is_staff:
        return redirect('home')
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
