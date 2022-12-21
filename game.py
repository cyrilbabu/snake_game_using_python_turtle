from turtle import Screen
from snake import Snake
from Food import Food
from score_board import Scoreboard
import time


def definitely():
    game_definitely = s.textinput(title="Definitely", prompt="easy/mid/hard")
    if game_definitely == "easy":
        return 0.3
    elif game_definitely == "mid":
        return 0.2
    elif game_definitely == "hard":
        return 0.1


s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
game_time = definitely()

s.listen()
s.onkey(key="Left", fun=snake.left)
s.onkey(key="Right", fun=snake.right)
s.onkey(key="Up", fun=snake.up)
s.onkey(key="Down", fun=snake.down)


while True:
    s.update()
    snake.snake_move()
    time.sleep(game_time)

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increse_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.update_high_score()
        snake.reset()

    for body in snake.snake_body[3:]:
        if snake.head.distance(body) < 10:
            score.update_high_score()
            snake.reset()
