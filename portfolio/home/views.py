from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Home, Projects, Contact
from django.contrib.auth.decorators import login_required


@login_required(login_url='login_page')
def home(request):
    details = Home.objects.all()
    projects = Projects.objects.all()

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        user = Contact.objects.create(
            name=name,
            email=email,
            message=message,
        )

        user.save()

        return redirect('home')

    return render(request, 'index.html', {'details':details, 'projects':projects})


@login_required(login_url='login_page')
def index(request):
    return HttpResponse('hello')