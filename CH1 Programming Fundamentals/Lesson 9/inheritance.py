class Parent():
    def __init__(self, last_name, eye_color):
        print "Parent Constructor Called"
        self.last_name = last_name
        self.eye_color = eye_color

class Child(Parent):
    def __init__(self, last_name, eye_color, toys):
        print "Child Constructor Called"
        Parent.__init__(self, last_name, eye_color)
        self.toys = toys

billy = Parent("Diaz", "black")
kid = Child("Diaz", "blue", 5)

print kid.last_name