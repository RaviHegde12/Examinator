from django.shortcuts import redirect
from .doc_sim import DocSim
from examinator.settings.common import MEDIA_ROOT
from gensim.models.keyedvectors import KeyedVectors
import nltk
from django.http import HttpRequest
from .views import generate_model_report


def word2vec(request):
    model_path = '/home/hasher/Documents/textbook_trained'
    w2v_model = KeyedVectors.load(model_path)

    ds = DocSim(w2v_model)

    df = open(MEDIA_ROOT + "/texts/blueprint.txt", "r")
    blueprint = df.read()
    df.close()

    # target_docs = [source_doc,'Beggar was so poor that he had no money' ,'Beggar was very rich and had lots of money', 'Beggar had nothing to buy slippers']

    df = open(MEDIA_ROOT + "/texts/answersheet.txt", "r")
    answer = df.read()
    df.close()

    answer = nltk.sent_tokenize(answer)
    print(answer)

    answer.append(blueprint)

    # This will return 3 target docs with similarity score
    sim_scores = ds.calculate_similarity(blueprint, answer)

    output = dict()
    output.update({'model': 'Word2vec', 'blueprint': blueprint, 'output': sim_scores})
    request = HttpRequest()
    request.output = output
    return generate_model_report(request)