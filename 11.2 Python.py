##file=open("test.txt","w") #w-write
##file.write("Hello") #если здесь написать вместо Hello на что-то другое,то слова просто перепишутся
##file.close()

##felix=open("test.txt","r") #r-read
##textt=felix.read()
##print(textt)
##felix.close()

##felix=open("test.txt","r")
####textt=felix.read()
##textt=felix.readline()
##print(textt)
##textt=felix.readline()
##print(textt)
##textt=felix.read(9)
##print(textt)
##felix.close()

felix=open("test.txt","r")
textt=felix.read()
a=textt.split("\n")
#split - разделяет (строчки,слова и тд) друг от друга
#\n-подели на строки
print(a[1])

b=textt.split(" ")
print(b)

c=textt.split()
print(c)

d=textt.split("a")
print(d)
