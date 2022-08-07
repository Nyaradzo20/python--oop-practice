'''class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):#self should be added to \every method you create
        print("My name is " + self.name)#self refers t\o whatever obj we are running a function on

r1 = Robot("tt", "yellow", 5)
r1.introduce_self()
r1 = Robot("jake", "cyan", 5)
'''
class Person:
    def __init__(self, n, p, i):
        self.name =n
        self.personality = p
        self.is_sitting = i
    def sit_dowm(self):
        self.is_sitting = True

    def stand_up(self):
        self.is_sitting = False

        print('false')

p1 = Person("bee", "aggressive", False)
p2 = Person("Alexa", "calm", True)
p1.stand_up()
        
