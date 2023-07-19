from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required()
def dashboard(request):
    if request.user.is_staff:
        return render(request, "pages/admin_dashboard.html")
    return render(request, "pages/dashboard.html")
