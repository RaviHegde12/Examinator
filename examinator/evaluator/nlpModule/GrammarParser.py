import nltk

class GrammarParser():

    def  __init__(self, grammarFilePath):
        self.grammar = nltk.data.load('file:./testcase/englishGrammar.cfg')
        self.parser = nltk.parse.chart.BottomUpLeftCornerChartParser(self.grammar)

    def parse(self, inp):
        return self.parser.parse(inp)


def ie_preprocess(document):
    sentences = nltk.sent_tokenize(document)
    tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
    sentences = [tokenizer.tokenize(sent) for sent in sentences]
    return sentences

inp = open("./testcase/testCasePollution.txt", 'r+').read()
parser = GrammarParser("./testcase/englishGrammar.cfg")
for sent in ie_preprocess(inp):
    for tree in parser.parse(sent):
        print(tree)
