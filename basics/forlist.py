'''sum=0
for i in range(1,6):
    sum=sum+i
print(sum)'''

a=[]
b=int(input())
for i in range(b):
    num=int(input("enter  the  value"+str(i+1)))
    a.append(num)
print(a)

sum=0 
for i in a:
    sum=sum+i
print(sum)

avg=0
avg = sum/b
print(avg)
