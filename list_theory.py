###3.1
##x=int(input())
##y=int(input())
##if x>0 and y>0:
##    print("I quadrant")
##elif x<0 and y>0:
##    print("II quadrant")
##elif x<0 and y<0:
##    print("III quadrant")
##elif x>0 and y<0:
##    print("IV quadrant")
##else:
##    print("It is a center")
###3.2
##a=int(input())
##if a==0:
##    print("It is zero")
##elif a%2==0:
##    print("even number")
##elif a%2==1:
##    print("odd number")
###3.3
animals=["cat","dog","turtle","bird"] #[]-list of sth
print(animals)

print(animals[2]) #нумерация начинается с 0
print(animals[1:4])
print(animals[2:])
print(animals[:4])

animals.append("fish") #это означает что я хочу добавить только fish в список animals
print(animals)

animals.remove("cat") #это означает что я хочу убрать cat из списока animals
print(animals)

animals.insert(3,"chicken") #тут мы добавляем chicken в определенную ячейку
print(animals)

del animals[4]
print(animals)

animals[1]="zebra" #изменить значение
print(animals)

animals.sort()              # сортирует
print(animals)

sorted(animals)     #sorted - сортирует, но не изменяет сам список

animals.reverse()
print(animals)

#reversed(animals)     #reversed - реверсит, но не изменяет сам список
#однако это спорно так как в курсах чето случилось нада погуглить

animals.extend(['chinchilla','horse'])  #тоже по одному добавляет в список
print(animals)                      #и нужно засунуть в список,а туда можно написать больше чем 1 элемент

integer=animals.index("zebra") #index-порядковый номер объекта,ind-переменная
print(integer)

if "cat" in animals: #not in-это означает "не в"
    print("There is a cat")
else:
    print("There is no cat")

print()
#animals.append(['dragon','chameleon'])
v=['a','b']+['c','d']                   #вместо списоков можно засунуть списковые переменные 
print(v)
v.pop()                     #убирает последнее
print()
print(v.pop())              #если мы так напишем, то он нам вернет не список, а то что убрал из списка
#так же если написать v.pop(0) то он уберет нулевой элемент

print(v[-1]) #это последний элемент списка
print(v[:-2])   #короче сама поймешь

a=[['','',''],['','',''],['','','']]
a[1][1]=1    #а красиво однако
print(a)

#b=[0,1,2,3,4,5,6,7,8,9]
b=list(range(10))        #тоже самое

print(b[:6:2])  #до шести и через 2
print(b[::-1])  #до конца и через -1
print(b[6:2:-1])#от шести до двух (по логике так нельзя, но у нас тут -1)
print(b[-2:])   #от предпоследней и до конца

b[3:7]=['a','b']#заменяем 3 числа на что-то другое
print(b)

s='qwerty'
print(s[3:])

s='cat/dog/frog'
s=s.split('/')    #если же мы хотим их разделить на пробелы, то ничего не пишем
print(s)

print('^'.join(['cat', 'dog', 'frog'])) #cat^dog^frog

txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three", 2)   #только первые one заменяет на three
print(x)

##Warning!
##
##нельзя соединять срезы x[2:7] и отдельные элементы x[1]





