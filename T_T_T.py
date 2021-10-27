#1

from colorama import Fore
import time
import random


T_T_T = [['-' , '-' , '-'] , 
         ['-' , '-' , '-'] ,
         ['-' , '-' , '-'] ]


x = Fore.RED + 'x'
o = Fore.BLUE + 'o'

def check_x():
    count_1 = 0

    for i in range(3):
        if T_T_T[i][0] == T_T_T[i][1] == T_T_T[i][2] == x:
            count_1 = 1
            break
        if T_T_T[0][i] == T_T_T[1][i] == T_T_T[2][i] == x:
            count_1 = 1
            break
        if T_T_T[2][0] == T_T_T[1][1] == T_T_T[0][2] == x:
            count_1 = 1
            break
        if T_T_T[2][2] == T_T_T[1][1] == T_T_T[0][0] == x:
            count_1 = 1
            break
    return count_1

def check_o():
    count_2 = 0

    for i in range(3):
        if T_T_T[i][0] == T_T_T[i][1] == T_T_T[i][2] == o:
            count_2 = 1
            break
        if T_T_T[0][i] == T_T_T[1][i] == T_T_T[2][i] == o:
            count_2 = 1
            break
        if T_T_T[2][0] == T_T_T[1][1] == T_T_T[0][2] == o:
            count_2 = 1
            break
        if T_T_T[2][2] == T_T_T[1][1] == T_T_T[0][0] == o:
            count_2 = 1
            break
    return count_2

def chech_w():
    p1 = check_x()
    p2 = check_o()
    
    if p1>p2:
        print(Fore.GREEN + "X WIN , Time: " + str( time.time() - start ))
        exit()
    elif p2>p1:
        print(Fore.GREEN + "O WIN , Time: " + str( time.time() - start ))
        exit()
    else:
        flag = True
        for i in range(3):
            for j in range(3):
                if T_T_T[i][j] == '-':
                    flag = False

        if flag == True and p1 == p2:
            print(Fore.BLACK + "DRAW , Time: " + str( time.time() - start ))
            exit()

def show():
        for i in range (3):
            for j in range (3):
                print(Fore.WHITE + T_T_T[i][j],end='')
            print()


print(Fore.WHITE + '1-vs 2-pc 3-PC')


op = int(input())

if op==1:

    print('vs')

    show()

    start = time.time()


    while True:

        while True:
            print( Fore.WHITE + 'p1:red X')
            
            m = int(input('m: '))
            n = int(input('n: '))

            if 1<=m<=3 and 1<=n<=3 :
                if T_T_T[m-1][n-1] == '-':
                    T_T_T[m-1][n-1] = x
                    break
                else:
                    print("full")
            else:
                print('wrong(1-3)')

        show()

        chech_w()


        while True:
            print(Fore.WHITE + 'p2:blue O')

            m = int(input('m: '))
            n = int(input('n: '))

            if 1<=m<=3 and 1<=n<=3 :
                if T_T_T[m-1][n-1] == '-':
                    T_T_T[m-1][n-1] = o
                    break
                else:
                    print("full")
            else:
                print('wrong(1-3)')

        
        show()

        chech_w()


if op == 2:

    print('pc')

    show()

    start = time.time()


    while True:

        while True:
            print( Fore.WHITE + 'p1:red X')
        
            m = int(input('m: '))
            n = int(input('n: '))

            if 1<=m<=3 and 1<=n<=3 :
                if T_T_T[m-1][n-1] == '-':
                    T_T_T[m-1][n-1] = x
                    break
                else:
                    print("full")
            else:
                print('wrong(1-3)')

        show()

        chech_w()


        while True:
            print(Fore.WHITE + 'pc:blue O')
            
            computer_rand_1 = random.randint(1,3)
            computer_rand_2 = random.randint(1,3)

            print('m: ' , computer_rand_1)
            print('n: ' , computer_rand_2)

            m = computer_rand_1
            n = computer_rand_2

            if T_T_T[m-1][n-1] == '-':
                T_T_T[m-1][n-1] = o
                break
            else:
                print("full")
            
        show()

        chech_w()

if op == 3:

    print('PC')

    print(Fore.BLACK + '___')    

    show()
    
    print()

    start = time.time()


    while True:

        while True:
            
            computer_rand_1 = random.randint(1,3)
            computer_rand_2 = random.randint(1,3)

            m = computer_rand_1
            n = computer_rand_2

            if T_T_T[m-1][n-1] == '-':
                T_T_T[m-1][n-1] = x
                break


        show()
        print()

        chech_w()


        while True:
            
            computer_rand_1 = random.randint(1,3)
            computer_rand_2 = random.randint(1,3)

            m = computer_rand_1
            n = computer_rand_2

            if T_T_T[m-1][n-1] == '-':
                T_T_T[m-1][n-1] = o
                break

        show()
        print()

        chech_w()
