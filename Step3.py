import urllib2
import requests
import json

def main():
    #requsting information from API
    payload = {'token':'aac0d88a55258415fc2556af0c0c65b9', 'needle':'', 'haystack': ''}
    data= requests.post("http://challenge.code2040.org/api/haystack", params = payload)

    #To view the information
    #print(data.text)

    #Coverting JSON string into Python dictionary
    dictionary = json.loads(data.text)

    #Split the dictionay into needle(target) and haystack(list of value)
    needle = dictionary["needle"]
    haystack = dictionary["haystack"]

    #Getting the index where the needle is located
    index = haystack.index(needle)

    #Checking needle, haystack, and index 
    #print(needle)
    #print(haystack)
    #print(index)

    #Posting my results
    load = {'token':'aac0d88a55258415fc2556af0c0c65b9', 'needle':index}
    requests.post("http://challenge.code2040.org/api/haystack/validate", params =load)
    

main()
