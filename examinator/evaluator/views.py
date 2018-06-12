import json
import os

from examinator.evaluator.Syntax_Checker.syntax_checker import syntax_check
from .AnswerProcessor.textProcessor import evaluation
from .AnswerProcessor.marksGenerator import markGenerator
from django.http import HttpResponse
from .OCR.image_to_text_converter import ImageToTextConverter
from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Document
from django.views.decorators.csrf import csrf_exempt
#from .AnswerProcessor.reportGenerator import report
#from reportlab.pdfgen import canvas
from .report.pdfReportGenerator import PdfReport
from .report.reportCardGenerator import ReportCard
from .report.detailedReportGenerator import DetailedReport
import re, math
from collections import Counter
from difflib import SequenceMatcher

WORD = re.compile(r'\w+')


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


            #fetching the name of the file
            for filename, file in request.FILES.items() :
                name = request.FILES[filename].name
            form.save()
            print("\n\n\n\n\n",name,"\n\n\n\n\n\n")
            ImageToTextConverter(name)

            #checking the grammar
            syntax_check("text_"+name+".txt")

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

        vector1 = text_to_vector(answer)
        vector2 = text_to_vector(blueprint)

        cosine = get_cosine(vector1, vector2)

        print('Cosine:', cosine)

        ratio = SequenceMatcher(None, answer, blueprint).ratio()

        print(ratio)

        if result.parse():
            data['result'] = 'success'
        else:
            data['result'] = 'failed'
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, "./testData/marksGenerator.json")
        result = markGenerator(json.load(open(filename, 'r')))
        # output = report(result.computeMarks())
        # output.generateReport()
        #DetailedReport(json.load(open(filename, 'r')), 'students').getPdf()
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        return HttpResponse("Request method is not post!")

def generate_report(request):
    response = HttpResponse(content_type='application/pdf')
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "./testData/marksGenerator.json")
    result = markGenerator(json.load(open(filename, 'r')))
    pdfFile = DetailedReport(json.load(open(filename, 'r')), 'subject').getPdf()
    response.write(pdfFile.read())
    pdfFile.close()
    return response

def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)

def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
    sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator
