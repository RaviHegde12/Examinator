from django.template import Template, Context

from rlextra.rml2pdf import rml2pdf
from io import StringIO
from reportlab.lib.utils import getBytesIO, isUnicode, asUnicode, asNative, asBytes, isPy3, unicodeT

class PdfReport():
    def __init__(self, result):
        self.result = result

    def getRML(self):
        """We used django template to write the RML, but you could use any other
        template language of your choice. 
        """
        t = Template(open('examinator/evaluator/report/hello.rml').read())
        c = Context(self.result)
        rml = t.render(c)
        #django templates are unicode, and so need to be encoded to utf-8
        return rml.encode('utf-8')
    
    def getPdf(self):
        rml = self.getRML()  
    
        buf = getBytesIO()
        
        #create the pdf
        rml2pdf.go(asBytes(rml), outputFileName=buf)
        pdfData = buf.getvalue()
        return pdfData