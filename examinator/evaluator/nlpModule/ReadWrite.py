import nltk

DIRECTORY = "steve_life"

class ReadWrite():
    def __init__(self, readFilePath, writeFilePath):
        self.readFile = open(readFilePath, 'r+')
        self.writeFile = open(writeFilePath, 'a')
    
    def readFromFile(self):
        return self.readFile.read()

    def writeToFile(self, posTaggedData):
        cfg = dict()
        for sentence in posTaggedData:
            for word, tag in sentence:
                if not cfg.__contains__(tag):
                    cfg.update({tag : set()})
                cfg[tag].add("'" + word.lower() + "'")
        for key in cfg.keys():
            strRepCfg = ""
            for word in cfg[key]:
                strRepCfg += word + ' | '
            self.writeFile.write("{0} -> {1}\n".format(key, strRepCfg[:len(strRepCfg) - 3]))

def ie_preprocess(document):
    lem = nltk.WordNetLemmatizer()
    sentences = nltk.sent_tokenize(document)
    tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
    sentences = [tokenizer.tokenize(sent) for sent in sentences]
    # lem_sents = [lem.lemmatize(word) for word in sent for sent in sentences]
    lem_sents = []
    for sent in sentences:
        wordList = []
        for word in sent:
            wordList.append(lem.lemmatize(word))
        lem_sents.append(wordList)
    sentences = [nltk.pos_tag(sent) for sent in lem_sents]
    stopwords = ['his', 'called', 'about', 'very', 'again']
    content = []
    for sent in sentences:
        wordList = []
        for taggedWord in sent:
            if taggedWord[0].lower() not in stopwords and taggedWord[1].lower() not in stopwords:
                wordList.append(taggedWord)
        content.append(wordList)
    return content

# f = ReadWrite("./testcase/testCasePollution.txt", "./testcase/englishGrammar.cfg")
# f.writeToFile(ie_preprocess(f.readFromFile()))

f = ReadWrite("./testcase/" + DIRECTORY + "/query.txt", "./testcase/" + DIRECTORY + "/q_grammar.cfg")
# f.writeToFile(ie_preprocess(f.readFromFile()))
print(ie_preprocess(f.readFromFile()))