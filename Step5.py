import datetime
import requests
import json

def main():
    #requsting information from API
    payload = {'token':'', 'datestamp':'', 'interval': ''}
    data= requests.post("http://challenge.code2040.org/api/dating", params = payload)

    #To view the information
    #print(data.text)

    #Coverting JSON string into Python dictionary
    dictionary = json.loads(data.text)

    #Split the dictionay into datestamp and interval
    datestamp = dictionary["datestamp"]
    interval = dictionary["interval"]

    #Creating the datestamp to use strptime 
    dateFormat = "%Y-%m-%dT%H:%M:%SZ"
    newDate = datetime.datetime.strptime(datestamp, dateFormat)

    #Changing interval to datetime seconds in order to add it with datestamp
    date = datetime.timedelta(seconds=interval) + newDate 

    #Reforming the date to ISO 8601 datestamp
    date = date.isoformat() + 'Z'
    
    #Checking my values
    #print(date)
    #print(newDate)
    #print(datestamp)
    #print(interval)

    #Posting my results
    load = {'token':'', 'datestamp':date}
    answer =requests.post("http://challenge.code2040.org/api/dating/validate", json =load)
    print(answer.text)
    

main()
