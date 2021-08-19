import requests
from dataclasses import dataclass
from typing import List
from models import Article


# @dataclass_json(undefined=Undefined.EXCLUDE)
# @dataclass
# class Article:
#     Id : int
#     MedienblattId : int
#     MedienblattLink : str

class MediaAccountClient(object):
    api_key: str
        
    base_url = 'http://api.media-account.de/api/'
    
    def __init__(self, api_key):
        self.api_key = api_key
        
    def articles(self, typ, von = None, bis = None, maxItems = 150, **kwargs):
        """
        Gibt ein Tuple zurück: Artikellist, Link zur nächsten 'seite', gesamtzahl
        """
        headers = {'api_key' : self.api_key}
        params = {'typ' : typ, 'von': von, 'bis':bis, 'maxItems' : maxItems}
        params.update(kwargs)
        
        response = requests.get(f'{self.base_url}v2/articles', headers = headers, params = params)
        response.raise_for_status()
        
        responseData = response.json()
        nextPageLink = responseData['NextPageLink']
        articles = list(map(lambda x: Article.from_dict(x), responseData['Items']))
        count = responseData['Count']

        return (articles, nextPageLink, count)
    
    
        
  
