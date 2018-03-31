class evaluation():

    def __init__(self, blueprint, answer):
        self.blueprint = blueprint
        self.answer = answer
    
    def parse(self):
        count=0
        for word in self.blueprint.split(' '):
            if word in self.answer:
                print(word)
                count += 1
        if(count == len(self.blueprint.split(' '))):
            return True
        return False