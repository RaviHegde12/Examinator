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


def homepage(request):
    return render(request, '../templates/home.html')


def model_form_upload(request, file_id):
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
            ImageToTextConverter(name)

            #checking the grammar
            syntax_check("text_"+name+".txt")

            # return redirect('process')
            fileuploaded = Document.objects.last()
            if (int)(file_id) == 1:
                filetype = "answer-sheet"
            else:
                filetype = "blueprint"
            return render(request, 'process.html',{'file': fileuploaded, 'file_type': filetype})

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

        if result.get_cosine()>0.5:
            data['result'] = 'success ' + str(result.get_cosine())
        else:
            data['result'] = 'failed ' + str(result.get_cosine())
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


def process(request):
    return render(request, 'process.html')
