import requests

city=input("Enter your city's name: ")

link="http://api.openweathermap.org/data/2.5/weather?&APPID=5e2620533f8da0deab17a137c456dbd0&units=metric&q="+city
data=requests.get(link)

#print(data)
#print(data.text)
d=data.json()
if d["cod"]==200:
    print(str(d["main"]["temp"])+"^C")
    print(str(d["wind"]["speed"])+"m/s")
else:
    print("This city in parallel world")
