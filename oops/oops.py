#Encapsulation

class person:

    def __init__(self,name,age):

        self.name=name
        self.__age=age   # set as private (encapsulation)

    
    def display_name(self):
        return self.name
    
    def change_name(self,name):
        self.name=name
    
    def display_age(self):
        return self.__age     
    

    def change_age(self,age):
        self.__age=age

    def display_details(self):

        print( (f"person : {self.name} , Age:{self.__age}"))


      

# inheritance
        
class student(person):   

    def __init__(self,name,age,regno):
        super().__init__(name,age)        
        self.regno=regno

    def display_student_details(self):
        super().display_details()
        return (f"student regno : {self.regno}")
    
        
    

p1=person("rohith",21)

s1=student("rohith",21,1945)
print(s1.display_student_details())
