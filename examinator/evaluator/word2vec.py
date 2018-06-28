from django.shortcuts import redirect

from .doc_sim import DocSim

from gensim.models.keyedvectors import KeyedVectors


def word2vec(request):
    model_path = '/home/hasher/Documents/textbook_trained'
    w2v_model = KeyedVectors.load(model_path)

    ds = DocSim(w2v_model)

    source_doc = 'Beggar had no money to buy chappals'
    target_docs = [source_doc,'Beggar was so poor that he had no money' ,'Beggar was very rich and had lots of money', 'Beggar had nothing to buy slippers']

    # This will return 3 target docs with similarity score
    sim_scores = ds.calculate_similarity(source_doc, target_docs)

    print(sim_scores)
    return redirect('homepage')