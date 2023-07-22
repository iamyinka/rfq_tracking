from django.shortcuts import render, redirect
from .forms import AddDonorForm
from .models import Donor

def add_donor(request):
    if not request.user.is_staff:
        return redirect('home')
    form = AddDonorForm()

    if request.method == "POST":
        form = AddDonorForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('home')

    context = {
        'form': form
    }
    return render(request, 'donors/create.html', context)

def donor_detail(request, donor_id):
    donor = Donor.objects.get(id=donor_id)
    rfps = donor.rfps.all()
    context = {
        "donor": donor,
        'rfps': rfps
    }
    return render(request, "donors/show.html", context)