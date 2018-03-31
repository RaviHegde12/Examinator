import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import DocumentForm
from django.views.decorators.csrf import csrf_exempt


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


@csrf_exempt
def generate(request):
    if request.method == 'POST':
        answer = request.POST.get('answer', None)
        blueprint = request.POST.get('blueprint', None)
        data = {}
        data['result'] = 'Successfully returned from views'
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        return HttpResponse("Request method is not post!")
