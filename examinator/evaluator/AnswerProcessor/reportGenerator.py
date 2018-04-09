# import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_pdf import PdfPages
#
# class report():
#
#     def __init__(self, result):
#         self.result = result
#
#     def generateReport(self):
#         report = self.convertResult()
#         pp = PdfPages('fig.pdf')
#         for student in report['students']:
#             fig, ax = plt.subplots()
#             fig.patch.set_visible(False)
#             ax.axis('off')
#             ax.axis('tight')
#             df = pd.DataFrame(data=report['students'][student])
#             ax.table(cellText=df.values, colLabels=df.columns, loc='center')
#             fig.tight_layout()
#             pp.savefig(fig)
#             plt.close(fig)
#         pp.close()
#
#     def convertResult(self):
#         report = dict()
#         report['students'] = dict()
#         print(self.result)
#         for student in self.result['students']:
#             report['students'][student] = dict()
#             report['students'][student]['Subject'] = list()
#             report['students'][student]['Max'] = list()
#             report['students'][student]['Obtained'] = list()
#             for subject in self.result['students'][student]:
#                 report['students'][student]['Subject'].append(subject)
#                 report['students'][student]['Max'].append(self.result['students'][student][subject]['maxMarks'])
#                 report['students'][student]['Obtained'].append(self.result['students'][student][subject]['marks'])
#         return report
#
