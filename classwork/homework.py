list1=["M","na","i","ke"]
list2=["y","me","s","lly"]
list3=[list1[i]+list2[i] for i in range(len(list1))]
list4=[]
def newlist():
        for x in list1:
           list4.append(x)
        for h in list2:
            list4.append(h)

list5=[x  for x in range(32) if x%3 ==0 ]
print(list5)
print(list3)
print(list4)


            
    