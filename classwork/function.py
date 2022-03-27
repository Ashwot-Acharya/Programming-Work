x=[10,20,30,40,5,25]
sum1=0
x.insert(2, 35)
for a in range(len(x)):
    sum1=sum1+ x[a]

print(x)
x.insert(35,3)
print(x)
b=x.pop(-1)
c=x.pop()
print(c)
print(b)
x.reverse()
print(x)
x.sort()
print(x)
sum = x[-3]+x[-2]+x[-1]
x.remove(20)
x.remove(5)
x.append(sum)
print(x)

    
         