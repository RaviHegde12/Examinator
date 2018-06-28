from django.shortcuts import redirect
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
from itertools import product
import pandas as pd
import numpy
import pickle


def process(request):
    df = open('/home/hasher/finalProject/Examinator/examinator/documents/images/text_Unit-test-blog-2.jpg.txt', "r")
    str1 = ""
    for line in df.readline():
        str1 = str1 + line
    # string1 = df['#1 String'].tolist()
    # string2 = df['#2 String'].tolist()
    # Quality = df['Quality'].tolist()
    df.close()
    df = open('/home/hasher/finalProject/Examinator/examinator/documents/images/blueprint.txt', "r")
    str2 = ""
    for line in df.readline():
        str2 = str2 + line
    df.close()
    sim_index = []
    stop_words = set(stopwords.words("english"))
    lemmatizer = WordNetLemmatizer()

    quality_calc = []

# for i in range(0, len(str1)):
    # str1 = str(string1[i])
    # str2 = str(string2[i])

    # with open("/media/nprathibha/Windows/w2vec/target_doc.txt", "wb") as fp:  # Pickling
    #     pickle.dump(str1, fp)
    # with open("/media/nprathibha/Windows/w2vec/source_doc.txt", "wb") as f:  # Pickling
    #     pickle.dump(str2, f)

    filtered_sentence1 = []
    filtered_sentence2 = []
    lemm_sentence1 = []
    lemm_sentence2 = []
    sims = []
    temp1 = []
    temp2 = []
    simi = []
    final = []
    same_sent1 = []
    same_sent2 = []

    for words1 in word_tokenize(str1):
        if words1 not in stop_words:
            if words1.isalnum():
                filtered_sentence1.append(words1)

    for i in filtered_sentence1:
        lemm_sentence1.append(lemmatizer.lemmatize(i))

    for words2 in word_tokenize(str2):
        if words2 not in stop_words:
            if words2.isalnum():
                filtered_sentence2.append(words2)

    for i in filtered_sentence2:
        lemm_sentence2.append(lemmatizer.lemmatize(i))

    for word1 in lemm_sentence1:
        simi = []
        for word2 in lemm_sentence2:
            sims = []

            syns1 = wordnet.synsets(word1)

            syns2 = wordnet.synsets(word2)
            for sense1, sense2 in product(syns1, syns2):
                d = wordnet.wup_similarity(sense1, sense2)
                if d != None:
                    sims.append(d)

            if sims != []:
                max_sim = max(sims)
                simi.append(max_sim)

        if simi != []:
            max_final = max(simi)
            final.append(max_final)

    similarity_index = numpy.mean(final)
    similarity_index = round(similarity_index, 2)
    '''print("Sentence 1: ",str1)
    print("Sentence 2: ",str2)
    print("Similarity index value : ", similarity_index)'''

    sim_index.append(similarity_index)

    '''if similarity_index>0.8:
        print("Similar")
    elif similarity_index>=0.6:
        print("Somewhat Similar")
    else:
        print("Not Similar")'''

    train = pd.DataFrame(
        {
            'str1': str1,
            'str2': str2,
            # 'Quality': Quality,
            'Our_quality': sim_index
        })

    print(sim_index)
    train.to_csv('./Wordnet_sim_results.csv', sep='\t')

    return redirect('homepage')
