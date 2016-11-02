import urllib2
import requests
import json

payload = {'token':'', 'github':'https://github.com/ThaliaVillalobos/code2040#code2040'}
r= requests.post("http://challenge.code2040.org/api/register", params = payload)
print(r.text)





