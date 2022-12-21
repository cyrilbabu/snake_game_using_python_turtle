from turtle import Turtle
STARTING_POSITION = [(0, 0), (20, 0), (40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.snake_body = []
        self.main_snake_body()
        self.head = self.snake_body[0]

    def main_snake_body(self):
        for i in STARTING_POSITION:
            self.add_body(i)

    def add_body(self, position):
        tim = Turtle("circle")
        tim.penup()
        tim.color("yellow")
        tim.goto(position)
        self.snake_body.append(tim)

    def extend(self):
        self.add_body(self.snake_body[-1].position())

    def snake_move(self):
        for snake in range(len(self.snake_body) - 1, 0, -1):
            x_coordinate = self.snake_body[snake - 1].xcor()
            y_coordinate = self.snake_body[snake - 1].ycor()
            self.snake_body[snake].goto(x_coordinate, y_coordinate)
        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        for seg in self.snake_body:
            seg.goto(1000,1000)
        self.snake_body.clear()
        self.main_snake_body()
        self.head = self.snake_body[0]

    def right(self):
        self.head.setheading(RIGHT)

    def left(self):
        self.head.setheading(LEFT)

    def up(self):
        self.head.setheading(UP)

    def down(self):
        self.head.setheading(DOWN)
