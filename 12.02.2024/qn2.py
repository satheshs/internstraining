def solve(persons):
    sorted_persons = dict(sorted(persons.items(), key=lambda item: item[1]['age']))
    return sorted_persons

number=int(input("Enter number of person: "))
persons={}
for i in range(number):
    name=input("Enter your name: ")
    age=int(input("Enter your age: "))
    persons[i+1]={
        "name":name,
        "age":age
    }
print(solve(persons))   