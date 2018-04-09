import json
import os

from .AnswerProcessor.textProcessor import evaluation
from .AnswerProcessor.marksGenerator import markGenerator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Document
from django.views.decorators.csrf import csrf_exempt
#from .AnswerProcessor.reportGenerator import report
#from reportlab.pdfgen import canvas
from .report.pdfReportGenerator import PdfReport
from django.db import connection


def homepage(request):
    return render(request, '../templates/home.html')


def model_form_upload(request):
    if request.method == 'POST':
        # f = request.FILES['file'].read()
        # print(f)
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            # file = request.FILES['file'].read()
            # print(file)
            form.save()
            # handle_uploaded_file(request.FILES['file'])
            return redirect('homepage')

    else:
        form = DocumentForm()
    return render(request, 'model_form_upload.html',{
        'form':form
    })


# def handle_uploaded_file(f):
#     with open('test.txt', 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)


def show_content(request):
    # pass
    objects = Document.objects.all()
    # for obj in objects:
    #     print(obj.description)
        # print(obj.display_document_content)
    return render(request, 'show_content.html', {'objects': objects})


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
        # output = report(result.computeMarks())
        # output.generateReport()
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        return HttpResponse("Request method is not post!")

def generate_report(request):
    response = HttpResponse(content_type='application/pdf')
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "./testData/marksGenerator.json")
    result = markGenerator(json.load(open(filename, 'r')))
    p = PdfReport(result.computeMarks())
    response.write(p.getPdf())
    return response
