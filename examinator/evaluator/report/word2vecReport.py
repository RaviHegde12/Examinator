import preppy
from .pdfReportGenerator import PdfReport
import os

class word2vecReportGenerator(PdfReport):
    def __init__(self, result, params):
        super().__init__(result, 'examinator/evaluator/report', 'word2vec.prep', 'word2vec-report.pdf', params)

    def clean(self):
        pass
