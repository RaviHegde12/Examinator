import json
import os
from .AnswerProcessor.textProcessor import evaluation
from .AnswerProcessor.marksGenerator import markGenerator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import DocumentForm
from django.views.decorators.csrf import csrf_exempt
from .AnswerProcessor.reportGenerator import report


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
        result = evaluation(blueprint, answer)
        if result.parse():
            data['result'] = 'success'
        else:
            data['result'] = 'failed'
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, "./testData/marksGenerator.json")
        result = markGenerator(json.load(open(filename, 'r')))
        output = report(result.computeMarks())
        output.generateReport()
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        return HttpResponse("Request method is not post!")
