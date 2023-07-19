from django.shortcuts import render, redirect
from .forms import AddDonorForm

def add_donor(request):
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