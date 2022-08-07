class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):#self should be added to every method you create
        print("My name is " + self.name)#self refers to whatever obj we are running a function on
        
r1 = Robot("tt", "yellow", 5)
r1.introduce_self()
'''
r1.name = "Tom"
r1.color = "red"
r1.weight = "30"
r1.introduce_self()

r2 = Robot()
r2.name = "jj"
r2.color = "blu"
r2.weight = "40"
r1.introduce_self()
'''
