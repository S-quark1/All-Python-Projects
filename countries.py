import requests

country=input("Write your country: ")
link="https://restcountries.eu/rest/v2/name/"+country
data=requests.get(link)
d=data.json()
#print(d["message"])
#if "Not Found" in d["message"]:
##if d["message"]=="Not Found":
##    print("This country in parallel world")
if "message" not in d:
    print("Capital:",d[0]["capital"])
    print("Code:",d[0]["currencies"][0]["code"])
    print("Language:",d[0]["languages"][0]["name"])
    print("Population:",d[0]["population"]/1000000,"million people")
else:
    print("This country is in parallel world")

