import preppy
import pdfkit

class PdfReport():
    def __init__(self, result):
        self.result = result

    def getHtml(self):
        template = preppy.getModule('examinator/evaluator/report/report.prep')
        html = template.getOutput({ 'students' : self.result})
        return html

    def getReport(self):
        html = self.getHtml();
        pdfkit.from_string(html, 'examinator/evaluator/report/report.pdf')
        return open('examinator/evaluator/report/report.pdf', 'rb').read()

    def getPdf(self):
        return self.getReport()

    