import json
import requests
from examinator.settings.common import KEY
from examinator.settings.common import MEDIA_ROOT

def syntax_check(file):
    f = open(MEDIA_ROOT + "/images/" + file,"r")
    f_json = open(MEDIA_ROOT + "/images/" + file + "_json.txt","w")
    data = f.readlines()
    f.close()
    for line in data :
        line = line.replace(" ","+")
        response = requests.get("https://api.textgears.com/check.php?text="+line+"&key=%20"+KEY)
        result = json.loads(response.content.decode('utf-8'))
        f_json.write(str(result) + "\n")
    f_json.close()
