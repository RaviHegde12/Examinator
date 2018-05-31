import re

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


answerpreprocessor()
