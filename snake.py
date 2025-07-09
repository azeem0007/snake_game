from turtle import Turtle
MOVE_DISTANCE =20

class Snake:
    def __init__(self):
        self.positions = [(0,0) , (-20,0) , (-40,0)]
        self.up_angle = 90
        self.down_angle = 270
        self.left_angle  =180
        self.right_angle  = 0
        self.segments =[]
        self.make_turtles()
        self.head = self.segments[0]


    def make_turtles(self):
        for position in self.positions:
            self.add_segment(position)
    def add_segment(self,position):
        new_segment = Turtle()
        new_segment.penup()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())


    def move_snake(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x_var = self.segments[seg_num - 1].xcor()
            y_var = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x_var, y_var)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading()!= self.down_angle:
            self.head.setheading(self.up_angle )

    def down(self):
        if self.head.heading() != self.up_angle:
            self.head.setheading(self.down_angle )

    def left(self):
        if self.head.heading() != self.right_angle:
            self.head.setheading(self.left_angle)

    def right(self):
        if self.head.heading() != self.left_angle:
            self.head.setheading(self.right_angle)
