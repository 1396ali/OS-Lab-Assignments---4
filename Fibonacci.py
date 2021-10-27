#4

n = int(input("n: "))

arry=[]

first = 0
second = 1

i = 0

print("Fibonacci: " , end='')
while i < n:
    arry.append(first)

    x = first + second

    first = second
    second = x
    i += 1

print(arry)