dictionary={"KZ":"Astana","RU":"Moscow","US":"Washington",}#ключ:значение

#другой способ создания словаря
dict2=dict([('a',1),('b',2)])
#theory_from lessons...exercises_My...list.py
print(dict2)
keys=['a','b','c']
values=[1,2,3]
zip(keys,values)   #возвращает нечто похожее на dict2
#or
dict2=dict(zip(keys,values))

d=dict(a=1,b=2)     #keys must be strings
#вернет нам {'a':1,'b':2}

print(dictionary['RU']) # все операции делаются через ключ

dictionary["GB"]="London" # если такого ключа нет, то добавить элемент
print(dictionary)

dictionary["KZ"]="Nur-Sultan" # если есть-заменяем значение
print(dictionary)

del dictionary['RU'] # для удаления используется только команды del
print(dictionary)

print(dictionary.pop('US'))  #принтанет нам не удаленный ключ, а его значение

print('')
for key in dictionary.keys(): #key-любая переменная
    print(key)
print('')
for hey in dictionary.values(): #hey-любая переменная
    print(hey)
print('')

for key in dictionary.keys():
    print(key,dictionary[key])
print("Is Russia still alive?")
if "RU" in dictionary.keys():
    print("Russia is still alive in that key list")
else:
    print("...")
if "London" in dictionary.values():
    print("London is still alive in that key list")
else:
    print("...")

d={'key1':1, 'key2':2.0, 'key3':[1,2,3]} #можем положить все что угодно
print(d['key1'])

##ключами могут быть не изменяемые типы данных
##такие как: 1,'abc', картеджи
##ключи должны быть уникальными

print(d.get('qqq','вернуть это если такого ключа нет'))
print(d.get('qqq'))  # тут он вернет None
#поиск происходит только по ключам

d1={'key1':33, 'f':{'a':1}, "tt": (1,2)}
d.update(d1)    #то чего нет добавляется, а что есть переписывается
print(d)

print(d.items())  #возвращает все пары ключа и значении в виде картриджа в списке
for k,v in d.items(): #картедж из переменных в k первое значение, в v второе
    print (k, '=',v)
print('')

#по ключам
for k,v in sorted(d1.items()): #sorted - сортирует
    print (k, '=',v)
#работает только если keys are the same cathegory
#подробнее в values

#по значениям через lambda
for k,v in sorted(dict2.items(),key=lambda x: x[1]):
    print (k, '=',v)
#values must be the same cathegory
#иначе выдаст ошибку типа:
# я не могу сравнивать 'str' и 'int' или с 'dict'












