import turtle

wn = turtle.Screen()
bob = turtle.Turtle()
turtle.speed(0)
my_start = (0, -100)

for i in range(20):
    angle_increment = 9
    bob.right(88 + angle_increment / 4)
    bob.forward(13 + angle_increment / 4)
    bob.left(50 + angle_increment / 4)
    bob.forward(88 + angle_increment / 4)
    bob.left(88 + angle_increment / 4)
    bob.forward(50 + angle_increment / 4)
    bob.right(48 + angle_increment / 4)
    bob.forward(33 + angle_increment / 4)
    bob.left(48 + angle_increment / 4)
    bob.forward(50 + angle_increment / 4)
    bob.left(40 + angle_increment / 4)
    bob.forward(88 + angle_increment / 4)
    bob.left(44 + angle_increment / 4)
    bob.forward(88 + angle_increment / 4)
    bob.left(50 + angle_increment / 4)
    bob.forward(50 + angle_increment / 4) 
    bob.left(40 + angle_increment / 4)
    bob.forward(33 + angle_increment / 2)
    bob.left(90 + angle_increment / 4)
    bob.forward(199 + angle_increment / 4)
    bob.left(99 + angle_increment / 4)
    bob.forward(90 + angle_increment / 4)
    bob.left(50 + angle_increment / 4)
    bob.forward(33 + angle_increment / 4) 
    bob.left(148 + angle_increment / 4)
    bob.forward(125 + angle_increment / 4)
    bob.left(99 + angle_increment / 4)
    bob.forward(148 + angle_increment / 4)
    bob.left(48 + angle_increment / 4)
    bob.forward(33 + angle_increment / 4)
    bob.left(90 + angle_increment / 4)
    bob.forward(66 + angle_increment / 4)
    bob.left(50 + angle_increment / 4)
    bob.forward(120 + angle_increment / 4)
    bob.left(48 + angle_increment / 4)
    bob.forward(99 + angle_increment / 4)

turtle.done()
