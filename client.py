import requests
from dataclasses import dataclass
from dataclasses_json import dataclass_json, Undefined
from typing import List


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class Article:
    Id : int
    MedienblattId : int
    MedienblattLink : str

class MediaAccountClient(object):
    api_key: str
        
    base_url = 'http://api.media-account.de'
    
    def __init__(self, api_key):
        self.api_key = api_key
        
    def articles(typ, von = None, bis = None, maxItems = 150, **kwargs):
        """
        Gibt ein Tuple zurück: Artikellist, Link zur nächsten 'seite', gesamtzahl
        """
        headers = {'api_key' : api_key}
        params = {'typ' : typ, 'von': von, 'bis':bis, 'maxItems' : maxItems}
        params.update(kwargs)
        
        var reponse = request.get(base_url, headers = headers, params = params)
        response.raise_for_status()
        
        responseData = response.json()
        nextPageLink = responseData['NextPageLink']
        articles = list(map(lambda x: Article.from_dict(x), responseData['Items']))
        count = responseData['Count']

        return (articles, nextPageLink, count)
    
    
        
  
