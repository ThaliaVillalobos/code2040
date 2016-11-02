import urllib2
import requests
import json

def main():
    #requsting information from API
    payload = {'token':'', 'prefix':'', 'array': ''}
    data= requests.post("http://challenge.code2040.org/api/prefix", params = payload)

    #To view information
    #print(data.text)

    #Coverting JSON string into Python dictionary
    dictionary = json.loads(data.text)

    #Split the dictionay into prefix(target) and array(list of value)
    prefix = dictionary["prefix"]
    array = dictionary["array"]

    #Creating a new array
    newArray = []

    #Created a loop to go through the array
    for i in range(len(array)):
        if(array[i].find(prefix) != 0): #If the words has the prefix word, I would not add it to my new array
            newArray.append(array[i])   #Adding the words that don't have the pefix by using the append


    #Checking my prefix, array and newArray
    #print(prefix)
    #print(array)
    #print(newArray)


    #Posting my results
    load = {'token':'', 'array':newArray}
    answer =requests.post("http://challenge.code2040.org/api/prefix/validate", json =load)
    print(answer.text)

main()
