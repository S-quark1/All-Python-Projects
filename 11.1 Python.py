import random
def Vse_s_vami_ponyatno():
    print(board[0],board[1],board[2])
    print(board[3],board[4],board[5])
    print(board[6],board[7],board[8])
def Random():
    while True:
        py=random.randint(0,8)
        if board[py]!="X" and board[py]!="O":
            board[py]='O'
            break
def Check(a):
    if board[0]==a and board[1]==a and board[2]==a:
        print("The",a,"won the competition!")
        return True
    elif board[3]==a and board[4]==a and board[5]==a:
        print("The",a,"won the competition!")
        return True
    elif board[6]==a and board[7]==a and board[8]==a:
        print("The",a,"won the competition!")
        return True
    elif board[0]==a and board[3]==a and board[6]==a:
        print("The",a,"won the competition!")
        return True
    elif board[0]==a and board[4]==a and board[8]==a:
        print("The",a,"won the competition!")
        return True
    elif board[6]==a and board[4]==a and board[2]==a:
        print("The",a,"won the competition!")
        return True
    elif board[1]==a and board[4]==a and board[7]==a:
        print("The",a,"won the competition!")
        return True
    elif board[2]==a and board[5]==a and board[8]==a:
        print("The",a,"won the competition!")
        return True
    else:
        return False
print("Let's play")
board=[1,2,3,4,5,6,7,8,9]

Vse_s_vami_ponyatno()
while True:
    my=int(input("Enter cell's number: "))
    if board[my-1]!='O' and board[my-1]!='X':
        board[my-1]='X' # or my=my-1
        Vse_s_vami_ponyatno()
        result=Check('X')
        if result==True:
            answer=input("Would u like to play again? (yes/no)")
            if answer=="yes":
                print("Ok")
                board=[1,2,3,4,5,6,7,8,9]
                Vse_s_vami_ponyatno()
            else:
                print("Bye")
                break
##    if board[0]=='X' and board[1]=='X' and board[2]!='X' and board[2]!='O':
##        board[2]=='O'
##    if board[2]=='X' or board[2]=='O':
##        Random()
        Random()
        print("I'll go:")
        Vse_s_vami_ponyatno()
        result=Check('O')
        if result==True:
            answer=input("Would u like to play again? (yes/no)")
            if answer=="yes":
                board=[1,2,3,4,5,6,7,8,9]
                Vse_s_vami_ponyatno()
            else:
                print("Bye")
                break
    else:
        print('Try again')
    
