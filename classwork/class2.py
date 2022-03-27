# lis =[]
# for x in range(12):
#     num= int(input("enter a number"))
#     lis.append(num)
# print(lis)
# for x in range(lis.__len__()):
#     lis[x]=lis[x]*lis[x]
# print(lis)

a = int(input("enter a range:"))
mylist=[]
for x in range(a):
    str=input("enter a string:")
    mylist.append(str)
newli =[]
for c in range(a):
    x = input("enter a stering:")
    newli.append(x)
vv=[]
for x in range(a):
    a = mylist[x]
    g = newli[x]
    vv.append(a)
    vv.append(g) 
print(vv)

