STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("orange")
        self.go_to_start()
        self.left(90)


    def go_to_start(self):
        self.goto(STARTING_POSITION)


    def move(self):
        self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y

