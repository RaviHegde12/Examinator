import nltk

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
    sentences = nltk.sent_tokenize(document)
    tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
    sentences = [tokenizer.tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    return sentences

f = ReadWrite("./testcase/testCasePollution.txt", "./testcase/englishGrammar.cfg")
f.writeToFile(ie_preprocess(f.readFromFile()))
