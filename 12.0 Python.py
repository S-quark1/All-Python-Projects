##file=open("Grades.txt","r")
##texture=file.read()
##file.close()
##c=texture.split()
##print(c)
##sum=0
##for n in c:
##    sum=sum+int(n)
##print(sum)
####for i in range(len(c)):
####    sum=sum+int(c[i])
####print(sum)
##print(sum/len(c))


f=open('example.txt','w')
f.write('abc\n')
f.writelines(['1\n','2\n','3\n'])

##f=open('example.txt','a')

##f=open('example.txt','r', encoding='utf-8') путь будет для русского языка
##f=open('example.txt','r+')  чтобы и писать и читать

f=open('example.txt','r')
print(f.read())
print('read')

f.seek(0)
print(str(f.readlines())+'-readlines')  #что тут творится?
f.seek(0)
print(f.readline()+'-readline')   #а то что она не возвращается назад к [0]
                      #а продолжает свой путь
print()               #и чтобы не путаться нужно каждый раз читать либо писать f.seek(0) 

f.seek(0)
for s in f:
    print(s)










