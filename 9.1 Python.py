import requests #ВСЕ ЧТО СТОИТ ПЕРЕД ЗНАКОМ = ЭТО ПЕРЕМЕННАЯ
import random

linkk="https://opentdb.com/api.php?amount=10&category=17&difficulty=easy&type=multiple"
data=requests.get(linkk)
dataa=data.json()
##print(dataa["results"][0]["question"])
##print(dataa["results"][0]["correct_answer"])
##print(dataa["results"][0]["incorrect_answers"])
#or
#drygaya_peremennaya_dlya_question=dataa["results"][0]["question"]
#print(drygaya_peremennaya_dlya_question)
counter=0
for i in range(10):
    question=dataa["results"][i]["question"]
    correct=dataa["results"][i]["correct_answer"]
    incorrect=dataa["results"][i]["incorrect_answers"]

    incorrect.append(correct)
    random.shuffle(incorrect)
    print(question)
    print("A)",incorrect[0])
    print("B)",incorrect[1])
    print("C)",incorrect[2])
    print("D)",incorrect[3])
    answer=input("Your answer: ")
    if answer==correct:
        print("Correct!")
        counter=counter+1
    else:
        print("Incorrect!")
        print("И я без понятия почему")
        print("There is correct answer",correct)
print("There is the number of correct answers:",counter)
if counter>=7:
    print("You are clever one")
elif counter<7 and counter>=3:
    print("You are not the smartest one")
elif counter<3:
    print("You are stupid")
##    ask=input("Would you like to play again? (yes/no) ")
##    if ask=='yes':
##        print("Ok!")
##    else:
##        print("Ok!")
##        break
    

