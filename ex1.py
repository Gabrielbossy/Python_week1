#Greeter: ask for name and favorite language, print a sentence using both.

# name = input("What is Your name? ")
# language = input("What is you favorite language? ")

# print(f"favorite Language for {name} is {language}! ")

import json

student = {
    "Name": "Peter",
    "Roll-no": "0090014",
    "Grade": "A",
    "Age": 20,
    "Subject": ["Computer Graphics", "Discrete Mathematics", "Data Structure"]
}

with open("data.json", "w") as write_file:
    json.dump(student, write_file, indent=4)

print(json.dumps(student, indent=4))