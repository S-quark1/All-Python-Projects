##2.1
##a=int(input("Enter a number: "))   # = оно говорит что это констант
##if a>0:
##    print("It's positive")  
##elif a<0:
##    print("It's negative")
##else:
##    print("It's 0")
##2.2
##login=input("Enter login: ") # == оно не утверждает
##password=input("Enter your password: ")
##if login=="Binara" or login=="Sanya" and password=="potato":
##    print("Go ahead")
##else:
###if login!="Tomato": # != это программа-не равняется
##    print("Error")
##2.3
percentage=int(input())
if percentage>100:
    print("You're crazy")
elif percentage>=90:
    print('A')
elif percentage>=75 and percentage<90:
    print('B')
elif percentage>=60 and percentage<75:
    print("C")
elif percentage>=50 and percentage<60:
    print("D")
elif percentage<=0:
    print("You're dummy and crazy")
else:
    print("F")

