from django.shortcuts import render,HttpResponse,redirect
from .models import Msg
from django.contrib.auth.models import User

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        textarea= request.POST.get('textarea')
        try:
            user = User.objects.create_user(name=name, email=email,subject=subject,textarea=textarea)
            user.save()
            
        except Exception as e:
            return HttpResponse(f"Error: {e}")

    return render(request, "index.html")