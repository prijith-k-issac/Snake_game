from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle()
            new_segment.shape("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.setpos(position)
            self.segments.append(new_segment)

    def add_segment(self, position):
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.setpos(position)
        self.segments.append(new_segment)

    def extend(self):
        # add a new segment
        self.add_segment(self.segments[-1].position())


    def move(self):

        # range(start =, stop =, step =) --> this function is from c++,
        # so it's not a pure python function, therefore when
        # using it, the usage of keyword is not allowed.

        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVING_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
