class Employee:
    __play = 100
    def __init__(self):
        self.id = 1
        self.salary = 1000
        self.designation = "worker"
        
    def travel(self):
        print(self.name)
        print(f"Employee travelling to mumbai")
        
obj1 = Employee() 

print(Employee._Employee__play)  # output: 100
print(obj1._Employee__play)  # we can also use it by object name also
# output = 100

# print(obj1.salary)

# obj1.travel()  # AttributeError: 'Employee' object has no attribute 'name'
# obj1.name = "aman"
# obj1.travel()   # output: aman

# we can create attribute(instance/class) outside the class and can be accessible inside the 
# class (but in case of instance u cannot use it in class unless you created it outside/inside the class)

# print(type(obj1))

# a = "aman"
# print(type(a))

# from demo_oops_project import Chat

# obj = Chat()