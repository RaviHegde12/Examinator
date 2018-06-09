#!~/final_year_project/Examinator/venv/bin/python3
import nltk

class PredicateEntityModel():
    def __init__(self, rawData):
        sentences = nltk.sent_tokenize(rawData)
        sentences = [nltk.word_tokenize(sent) for sent in sentences]
        self.tagged_sents = [nltk.pos_tag(sent) for sent in sentences]
        self.ner_tagged_sents = [nltk.ne_chunk(sent) for sent in self.tagged_sents]
        print(self.ner_tagged_sents)

PredicateEntityModel(open("./testcase/testCasePollution.txt", 'r+').read())