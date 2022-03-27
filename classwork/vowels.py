stringList=["apple","mango","banana","cow","dog","deer","falcon","cars","books"]
n=0

newlist=[]
for x in stringList:
    for z in x:
        if z.lower() == "a" or z.lower()=="e" or z.lower()=="i" or z.lower()=="o" or z.lower()=="u":
            n = n+1
    if n>1:
        print(x)
        newlist.append(x)
    n=0

print(newlist)
    
                
            