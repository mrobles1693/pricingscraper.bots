import requests
import json

from Service.ApiResponse import ApiResponse

_urlBase = 'https://rspricingscraper.azurewebsites.net/api/BotRs/'
_apiresp = ApiResponse()

def iniBotExecution():
    urlReq = _urlBase + 'getIdBotExecution'
    response = requests.get(url=urlReq)
    return _apiresp.from_json(response.json())

def getListSimilar():
    urlReq = _urlBase + 'getListSimilar'
    response = requests.get(url=urlReq)
    return _apiresp.from_json(response.json())

def insRegistroPrecio(registroPrecio):
    urlReq = _urlBase + 'postInsRegistroPrecio'
    response = requests.post(url=urlReq, data=json.dumps(registroPrecio))
    return _apiresp.from_json(response.json())

def finBotExecution(nIdBotExecution):
    urlReq = _urlBase + 'finBotExecution'
    args = { 'nIdBotExecution' : nIdBotExecution }
    response = requests.get(url=urlReq, params=args)
    return _apiresp.from_json(response.json())
