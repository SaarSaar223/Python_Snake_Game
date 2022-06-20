from turtle import Turtle

turtle_positions = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
WAIT_TIME = 0.07
import time

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.moving_right = True
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def create_snake(self):
        for position in turtle_positions:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def createnewsegment(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(self.segments[len(self.segments) - 1].pos())
        self.segments.append(new_segment)

    def move(self):
        turtcopy = []
        for turts in self.segments:
            turtcopy.append(turts.pos())

        for n in range(len(self.segments)):
            if n == 0:
                self.segments[n].forward(MOVE_DISTANCE)
            else:
                self.segments[n].goto(turtcopy[n - 1])

        turtcopy.clear()

    def wall_collision(self):
        if self.segments[0].xcor() > 300 or self.segments[0].xcor() < -300:
            return True
        elif self.segments[0].ycor() > 300 or self.segments[0].ycor() < -300:
            return True
        else:
            return False

    def tail_collision(self):
        for n in range(len(self.segments)):
            if n == 0:
                pass
            elif self.segments[0].distance(self.segments[n]) < 10:
                return True

        return False


    def up(self):
        if self.moving_up or self.moving_down:
            pass
        else:
            self.moving_up = True
            self.moving_left = False
            self.moving_right = False
            self.segments[0].seth(90)

        time.sleep(WAIT_TIME)

    def down(self):
        if self.moving_up or self.moving_down:
            pass
        else:
            self.moving_down = True
            self.moving_left = False
            self.moving_right = False
            self.segments[0].seth(270)

        time.sleep(WAIT_TIME)

    def left(self):
        if self.moving_left or self.moving_right:
            pass
        else:
            self.moving_left = True
            self.moving_up = False
            self.moving_down = False
            self.segments[0].seth(180)
        time.sleep(WAIT_TIME)

    def right(self):
        if self.moving_left or self.moving_right:
            pass
        else:
            self.moving_right = True
            self.moving_up = False
            self.moving_down = False
            self.segments[0].seth(0)
        time.sleep(WAIT_TIME)

