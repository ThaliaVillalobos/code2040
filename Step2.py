import urllib2
import requests
import json

def main():
    #requsting string from API
    payload = {'token':'', 'string':''}
    data= requests.post("http://challenge.code2040.org/api/reverse", params = payload)

    #printing out the string given
    word = data.text
    print(word)

    #printing out the reverse string
    newWord = reverse_string(word)
    print(newWord)
    

def reverse_string(strWord):
    return strWord[::-1]


main()

