#3

m = int(input("m:"))
n = int(input("n:"))

def Table(m,n):
	for i in range(1,m+1):
		for j in range(1,n+1):
			print(i*j, end='\t')
		print()
        
Table(m,n)