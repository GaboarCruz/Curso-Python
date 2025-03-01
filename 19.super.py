class LivingBeing:
    def __init__(self, name):
        self.name = name

class Person(LivingBeing): 
    def __init__(self,name,age):    
        super().__init__(name)
        self.age = age

    def greet(self):
        print("Hello! i am a person")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def greet(self):
        super().greet()
        print(f"Hello, my student ID is {self.student_id}")

student = Student("Ana", 20, "S123")
student.greet()