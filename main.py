import time
import turtle as t
from snake import Snake
from food import Food
from score_board import ScoreBoard

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Catafo\'s Snake Game')
screen.tracer(0)

snakes = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snakes.up, "Up")
screen.onkey(snakes.down, "Down")
screen.onkey(snakes.left, "Left")
screen.onkey(snakes.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snakes.move()

    # Detect collision
    if snakes.snake_head.distance(food) < 15:
        food.refresh()
        snakes.extend()
        scoreboard.increase_score()

    # Detect detect collision with wall
    if snakes.snake_head.xcor() > 280 or snakes.snake_head.xcor() < -280 or snakes.snake_head.ycor() > 280 or snakes.snake_head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # detect collision with tail
    for body in snakes.snake[2:]:
        if snakes.snake_head.distance(body) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
