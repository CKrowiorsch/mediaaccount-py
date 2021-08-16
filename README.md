# MediaAccount Python Client

## Usage

```python
import datetime

apiKey = '123456789'
mediaAccount = MediaAccountClient(key=apiKey)

# raw client
(articles, nextPageLink, count) = mediaAccount.articles('ImportDatum', von=datetime(2021,1,1), bis=datetime(2021,2,1), maxItems=10)
mediaAccount.articleNext(nextPageLink)

```

## Development

### TODO

* Iterator
* V3 API
