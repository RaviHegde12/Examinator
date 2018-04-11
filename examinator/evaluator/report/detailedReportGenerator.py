import preppy
from .pdfReportGenerator import PdfReport
import os

class DetailedReport(PdfReport):

    def __init__(self, result, params):
        super().__init__(result, 'examinator/evaluator/report', 'detail-report.prep', 'detail-report.pdf', params)

    def calculateTotalMarks(self):
        for student in self.result['students']:
            for subject in student['subjects']:
                totalMarks = 0
                for answer in subject['answerBooklet']:
                    marks = 0
                    for statement in answer['statements']:
                        marks += answer['maxMarks'] * statement['correctness'] * statement['marks']
                    marks = round(marks)
                    answer['marks'] = marks
                    totalMarks += marks
                subject['totalMarks'] = totalMarks
                

    def getHtml(self):
        template = preppy.getModule(self.prepFileDir + '/' + self.prepFileName)
        self.pages = []
        self.calculateTotalMarks()
        for student in self.result['students']:
            for subject in student['subjects']:
                temp_html = template.getOutput({ self.prepParamVar : subject, 'studentId': student['id']})
                html_file = self.prepFileDir + '/' + str(student['id']) + '-' + str(subject['id']) + '.html'
                html_write = open(html_file, 'w')
                html_write.write(temp_html)
                html_write.close()
                self.pages.append(html_file)
        return self.pages

    def clean(self):
        for file in self.pages:
            os.remove(file)