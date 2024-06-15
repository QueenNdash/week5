class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and {self.gender}.")
        
# Creating an instance of Person
person = Person("Rabbeca", 18, "female")

# Calling introduce method to display the introduction
person.introduce()
