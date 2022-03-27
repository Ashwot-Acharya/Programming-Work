import json
import pprint

student = {
    "ram":{'age':12 ,"grade":6 },
    "shyam":{'age':15,"grade":2},
    "hari":{'age':18,"grade":8},
    "samrat":{'age':17 , "grade":10  },


}
for x in student.keys():
    print(x)

for x in student.values():
    print(x)
for x in student.items():
    print(x)

student['samrat']={'age': 17, 'grade':12 }
for x in student.values():
    print(x)
    

pprint.pprint(student)
