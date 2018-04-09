import re


def answerpreprocessor():
    s = "Register Number: 14GAEC9043 Subject: Chemistry Subject Code: 708642 Date: 08/04/2018"
    u = re.compile("Register Number:(.*)$")
    x = u.search(s).group(1)[:11]
    print(x.strip())
    v = re.compile("Subject Code:(.*)$")
    y = v.search(s).group(1)[:7]
    print(y.strip())


answerpreprocessor()
