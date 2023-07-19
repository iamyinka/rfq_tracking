from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from donors.models import Donor

@login_required()
def dashboard(request):
    donors = Donor.objects.all()
    context = {
        'donors': donors
    }
    
    if request.user.is_staff:
        return render(request, "pages/admin_dashboard.html", context)
    return render(request, "pages/dashboard.html", context)
