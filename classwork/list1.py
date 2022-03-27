z=["ram","shyam","reet","geet","subr","hari"]
n=[]
for x in z:
    for c in x:
        if(c=="a"):
            n.append(x)
print(n)

ciw=[5,10,20,80,20,79,30,20]
var=ciw.index(20)
print(var)
ciw[var]=200
print(ciw)

vat= "this is a cow and i love cows "
c=vat.split()
print(c)

cowlist=[v for v in z if "a" in v ]
print(cowlist)