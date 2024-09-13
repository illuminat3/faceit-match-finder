import requests

def GetTextFromUrlRequest(url):
    response = requests.get(url)

    if response.status_code == 200:
       return response.text
    
    return None

def GetJsonFromUrlRequest(url):
    response = requests.get(url)

    if response.status_code == 200:
        return response.json
    
    return None