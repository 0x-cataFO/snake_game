import turtle as t
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.snake_head = self.snake[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_body(position)

    def add_body(self, position):
        tut = t.Turtle('turtle')
        tut.color('white')
        tut.pu()
        tut.goto(position)
        self.snake.append(tut)

    def extend(self):
        self.add_body(self.snake[-1].position())

    def move(self):
        for body in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[body - 1].xcor()
            new_y = self.snake[body - 1].ycor()
            self.snake[body].goto(new_x, new_y)
        self.snake_head.forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.seth(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.seth(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.seth(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.seth(RIGHT)
