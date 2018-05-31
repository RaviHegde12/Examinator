import re

<<<<<<< 75c2c5f03f28ddc62a166f583b28e8b5065991cf

def answerpreprocessor():
    s = "Register Number: 14GAEC9043 Subject: Chemistry Subject Code: 708642 Date: 08/04/2018"
    u = re.compile("Register Number:(.*)$")
    x = u.search(s).group(1)[:11]
    print(x.strip())
    v = re.compile("Subject Code:(.*)$")
    y = v.search(s).group(1)[:7]
    print(y.strip())
=======
'''Method to pick register number and subject code
    Need to give input in the following format (space after :)
'''
def answerpreprocessor():
    s = "Name: Ravi Register Number: 14GAEC9043 Subject Code: 000777 Date: 09/04/2018"
    # v = s.split("Register Number:",1)[1]
    # print(v[:11])
    # u = s.split("Subject Code:",1)[1]
    # print(u)
    v = re.compile("Register Number:(.*)$")
    u = re.compile("Subject Code:(.*)$")
    print(v.search(s).group(1)[:11])
    print(u.search(s).group(1)[:7])
>>>>>>> Added method to pick register num and sub code


answerpreprocessor()
