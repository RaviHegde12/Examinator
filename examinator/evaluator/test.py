import nltk
text = "This is Ravi. He lives in Bangalore."


def get_entity(text):
    tokens = nltk.tokenize.word_tokenize(text)
    tagged_sent = nltk.pos_tag(tokens)
    # sentt = nltk.ne_chunk(tagged_sent, binary=False)
    # print(sentt)

    nouns = [word for word, pos in tagged_sent if pos == 'NNP']
    nouns = set(nouns)
    dict_names = {}
    for index, name in enumerate(nouns):
        dict_names[name] = "ent"+str(index)
    for key in dict_names.keys():
        text = text.replace(key, dict_names[key])
    print(text)


get_entity(text)
