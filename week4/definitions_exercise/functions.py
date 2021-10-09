import requests
from urllib.parse import quote

def define(term):
    definition = None
    partofspeech = None

    baseurl = "https://api.dictionaryapi.dev/api/v2/entries/en_US/"

    json = requests.get(baseurl + quote(term)).json()

    if "title" in json:
        definition = ""
    else:
        try:
            partofspeech = json[0]['meanings'][0]['partOfSpeech']
            definition = "(" + partofspeech + ") " + json[0]['meanings'][0]['definitions'][0]['definition']
        except:
            try:
                definition = json[0]['meanings'][0]['definitions'][0]['definition']
            except:
                definition = ""

    return definition


def get_list():
    content = open('list.txt', "r", encoding='utf-8-sig').read()
    return content
