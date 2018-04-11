import preppy
from .pdfReportGenerator import PdfReport
import os

class ReportCard(PdfReport):

    def __init__(self, result, params):
        super().__init__(result, 'examinator/evaluator/report', 'report-card.prep', 'report-card.pdf', params)

    def getHtml(self):
        template = preppy.getModule(self.prepFileDir + '/' + self.prepFileName)
        self.pages = []
        for student in self.result['students']:
            temp_html = template.getOutput({ self.prepParamVar : self.result, 'student': student})
            html_file = self.prepFileDir + '/' + str(student) + '.html'
            html_write = open(html_file, 'w')
            html_write.write(temp_html)
            html_write.close()
            self.pages.append(html_file)
        return self.pages

    def clean(self):
        for file in self.pages:
            os.remove(file)