#1

from colorama import Fore
import time
import random


T_T_T = [['-' , '-' , '-'] , 
         ['-' , '-' , '-'] ,
         ['-' , '-' , '-'] ]

x = Fore.RED + 'x'
o = Fore.BLUE + 'o'


def check_1():
    if T_T_T[2][0] == x and T_T_T[1][1] == x and T_T_T[0][2] == x :
        print(Fore.GREEN + "X WIN , Time: " + str( time.time() - start ))
        exit()
    elif T_T_T[2][2] == x and T_T_T[1][1] == x and T_T_T[0][0] == x :
        print(Fore.GREEN + "X WIN , Time: " + str( time.time() - start ))
        exit()

    for i in range(3):
        if T_T_T[i][0] == x and T_T_T[i][1] == x and T_T_T[i][2] == x :
            print(Fore.GREEN + "X WIN , Time: " + str( time.time() - start ))
            exit()
    for j in range (3):
        if T_T_T[0][j] == x and T_T_T[1][j] == x and T_T_T[2][j] == x :
            print(Fore.GREEN + "X WIN , Time: " + str( time.time() - start ))
            exit()
    

def check_2():
    if T_T_T[2][0] == o and T_T_T[1][1] == o and T_T_T[0][2] == o :
        print(Fore.GREEN + "O WIN , Time: " + str( time.time() - start ))
        exit()
    elif T_T_T[2][2] == o and T_T_T[1][1] == o and T_T_T[0][0] == o :
        print(Fore.GREEN + "O WIN , Time: " + str( time.time() - start ))
        exit()

    for i in range(3):
        if T_T_T[i][0] == o and T_T_T[i][1] == o and T_T_T[i][2] == o :
            print(Fore.GREEN + "O WIN , Time: " + str( time.time() - start ))
    for j in range (3):
        if T_T_T[0][j] == o and T_T_T[1][j] == o and T_T_T[2][j] == o :
            print(Fore.GREEN + "O WIN , Time: " + str( time.time() - start ))
            exit()

def show():
        for i in range (3):
            for j in range (3):
                print(Fore.WHITE + T_T_T[i][j],end='')
            print()


print(Fore.WHITE + '1-vs 2-pc')


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
        check_1()


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
        check_2()



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
        check_1()

        
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
        check_2()