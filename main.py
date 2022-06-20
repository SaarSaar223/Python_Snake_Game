from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



game_running = True
score = 0

while game_running:
    screen.update()
    snake.move()
    time.sleep(0.1)
    if snake.segments[0].distance(food) < 30:
        food.refresh()
        score += 1
        scoreboard.updatescore(score)
        snake.createnewsegment()
    if snake.wall_collision() or snake.tail_collision():
        scoreboard.gameovermessage();
        game_running = False;
screen.exitonclick()