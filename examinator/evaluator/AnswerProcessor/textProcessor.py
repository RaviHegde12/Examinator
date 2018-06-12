import re, math
from collections import Counter
from difflib import SequenceMatcher

WORD = re.compile(r'\w+')


class evaluation():

    def __init__(self, blueprint, answer):
        self.blueprint = blueprint
        self.answer = answer

    def parse(self):
        count=0

        # for word in self.blueprint.split(' '):
        #     if word in self.answer:
        #         print(word)
        #         count += 1
        # if(count == len(self.blueprint.split(' '))):
        #     return True
        # return False

    def text_to_vector(self, text):
        words = WORD.findall(text)
        return Counter(words)

    def get_cosine(self):
        vec1 = self.text_to_vector(self.answer)
        vec2 = self.text_to_vector(self.blueprint)

        intersection = set(vec1.keys()) & set(vec2.keys())
        numerator = sum([vec1[x] * vec2[x] for x in intersection])

        sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
        sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
        denominator = math.sqrt(sum1) * math.sqrt(sum2)

        if not denominator:
            return 0.0
        else:
            return float(numerator) / denominator

    #cosine = get_cosine()

    # print('Cosine:', cosine)
    #
    # ratio = SequenceMatcher(None, answer, blueprint).ratio()
    #
    # print(ratio)
