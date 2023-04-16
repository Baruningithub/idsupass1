def digitsum(n):
    sum=0
    for i in str(n):
        sum=sum+int(i)
    return sum
l=int(input("Enter lower range: "))
u=int(input("Enter upper range: "))
a=[]

for x in range(l,u+1):
    if (int(x**0.5)**2)==x:
        if digitsum(x)<10:
            a.append(x)
print(a)
