from django.db import models


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='document/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def display_document_content(self):
        with open(self.document.path) as fp:
            return fp.read().replace('\n', '<br/>')
    # self.document.open()
    # return self.text.read().replace('\n', '<br>')
    #     self.document.open()
    #     return self.document.file.read().replace('\n', '<br>')
    #     fp = open(self.document.path)
    #     return fp.read().replace('\n', '<br/>')
