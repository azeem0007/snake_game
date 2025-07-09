from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.colors = ["blue" , "orange" , "green" , "white" , "violet" , "purple"]
        self.shape("turtle")
        self.color("red")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.speed(10)

    def randomness(self):
        x_cord = random.randint(-280, 280)
        y_cord = random.randint(-280, 280)
        self.color(random.choice(self.colors))
        self.goto(x_cord, y_cord)