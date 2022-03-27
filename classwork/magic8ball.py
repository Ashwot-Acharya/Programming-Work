import random 
import threading
option=["Yes","no","maybe","it is certain","certainly not "]
a = input("enter your question")
print(a)
rand = random.randint(0, len(option))
print(option[rand])





