class markGenerator():
    def __init__(self, booklets):
        self.booklets = booklets
        self.result = dict()

    def computeMarks(self):
        self.result.update({ 'students': dict() })
        for student in self.booklets['students']:
            self.result['students'].update({ student['id']: dict() })
            self.result['students'][student['id']].update({ 'total': dict() })
            self.result['students'][student['id']]['total']['maxMarks'] = 0
            self.result['students'][student['id']]['total']['marks'] = 0
            for subject in student['subjects']:
                self.result['students'][student['id']].update({ subject['id']: dict() })
                self.result['students'][student['id']][subject['id']]['marks'] = 0
                self.result['students'][student['id']][subject['id']]['maxMarks'] = subject['maxMarks']
                self.result['students'][student['id']]['total']['maxMarks'] += subject['maxMarks']
                for answerBooklet in subject['answerBooklet']:
                    for sentence in answerBooklet['statements']:
                        self.result['students'][student['id']][subject['id']]['marks'] += \
                            round(answerBooklet['maxMarks'] * sentence['correctness'] * sentence['marks'])
                self.result['students'][student['id']]['total']['marks'] += \
                    self.result['students'][student['id']][subject['id']]['marks']
        return self.result