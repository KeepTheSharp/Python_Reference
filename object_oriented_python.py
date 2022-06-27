# object_oriented_python.py


class Person:
    pass

#create an instance
p = Person()

# p is an object of Person class
print(p)    #  prints    <__main__.Person object at 0x2123923)


# self refers to itself

class MyPerson:
    def getName(self):        # self is a must here      it is like MyPerson.getAge()
        print("Avi")
        return

    def getAge(self):
        print("16")

mp = MyPerson()

mp.getName()        # prints Avi
mp.getAge()         # prints 16


# Class constructor __init__(self, parameters )
# init of class
class HeyPerson:
    def __init__(self, name, age):    # this is like a constructor
        self.name = name
        self.age = age

    def getName(self):
        print("Your name is " + self.name)

    def getAge(self):
        print("Your age is " , self.age)     #   used ","    self.age is number


hp = HeyPerson("Bob",22)
hp.getName()          # prints Your name is Bob
hp.getAge()           # prints Your age is 22


# ----------------------------------------------------------------------
# Inheritance

class Parent:
    def __init_(self):
        print("This is the parent class")
    def parentFunc(self):
        print("This is the parent func")

p = Parent()
p.parentFunc()    # prints   This is the parent func

class Child(Parent):    # child class, inherits Parent class
    def __init__(self):
        print("This is the child class")
    def childFunc(self):
        print("This is the child func")

c = Child()     # prints  This is the child class


#--
class Parent2:
    def __init__(self):
        pass

    def test(self):
        print("parent")

class Child2(Parent2):
    def __init__(self):
        pass

    def test(self):
        print("child")


c = Child2()
c.test()        # this will print child.  overrides the parent



