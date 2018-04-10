import preppy
import pdfkit

class PdfReport():
    def __init__(self, result, prepFileDir, prepFileName, outputFileName, prepParamVar):
        self.result = result
        self.prepFileDir = prepFileDir
        self.prepFileName = prepFileName
        self.outputFileName = outputFileName
        self.prepParamVar = prepParamVar

    def getHtml(self):
        template = preppy.getModule(self.prepFileDir + '/' + self.prepFileName)
        html = template.getOutput({ self.prepParamVar : self.result})
        return html

    def getReport(self):
        html = self.getHtml()
        pdfkit.from_file(html, self.prepFileDir + '/' + self.outputFileName)
        self.clean()
        return open(self.prepFileDir + '/' + self.outputFileName, 'rb')

    def getPdf(self):
        return self.getReport()

    