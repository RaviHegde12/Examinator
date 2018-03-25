from django.shortcuts import render, redirect
from .forms import DocumentForm


def homepage(request):
    return render(request, '../templates/home.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('homepage')

    else:
        form = DocumentForm()
    return render(request, 'model_form_upload.html',{
        'form':form
    })
