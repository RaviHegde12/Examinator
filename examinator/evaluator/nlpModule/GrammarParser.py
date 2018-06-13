import nltk

DIRECTORY = "steve_life"

class GrammarParser():

    def  __init__(self, grammarFilePath):
        self.grammar = nltk.data.load('file:' + grammarFilePath)
        self.parser = nltk.parse.chart.BottomUpLeftCornerChartParser(self.grammar)

    def parse(self, inp):
        return self.parser.parse(inp)


def ie_preprocess(document):
    lem = nltk.WordNetLemmatizer()
    sentences = nltk.sent_tokenize(document)
    tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
    sentences = [tokenizer.tokenize(sent) for sent in sentences]
    lem_sents = []
    for sent in sentences:
        wordList = []
        for word in sent:
            wordList.append(lem.lemmatize(word))
        lem_sents.append(wordList)
    stopwords = ['his', 'called', 'about', 'very', 'again']
    # content = [word for word in sent for sent in sentences if word.lower() not in stopwords]
    content = []
    for sent in lem_sents:
        wordList = []
        for taggedWord in sent:
            if taggedWord.lower() not in stopwords:
                wordList.append(taggedWord.lower())
        content.append(wordList)
    return content


inp = open("./testcase/" + DIRECTORY + "/passage.txt", 'r+').read()
parser = GrammarParser("./testcase/" + DIRECTORY + "/grammar.cfg")

parseTree = []
# print(ie_preprocess(inp))
for sent in ie_preprocess(inp):
    for tree in parser.parse(sent):
        print(tree)
