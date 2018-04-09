from django.template import Template, Context
import preppy
from io import StringIO

class PdfReport():
    def __init__(self, result):
        self.result = result

    def getReport(self):
        """We used django template to write the RML, but you could use any other
        template language of your choice.
        """
        template = preppy.getModule('examinator/evaluator/report/report.prep')

        html = template.getOutput({ 'students' : self.result})

        #t = Template(open('examinator/evaluator/report/hello.rml').read())
        #c = Context(self.result)
        #rml = t.render(c)
        #django templates are unicode, and so need to be encoded to utf-8
        #return rml.encode('utf-8')
        return html

    def getPdf(self):
        html = self.getReport()

        #create the pdf
        #rml2pdf.go(asBytes(rml), outputFileName=buf)
        #pdfData = buf.getvalue()
        return html
