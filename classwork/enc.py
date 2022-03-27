v = input("enter a a sentence:")
c = input("enter a key")
key=[]
string=""
enc=[]
f=""
enc.append(c)
for b in v:
    ec = ord(b)+12
    string =string+ chr(ec)
print(string)
for x in string:
    dec = ord(x)-12
    f = f+chr(dec)
print(f)