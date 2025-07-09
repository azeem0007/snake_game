from snake import Snake
from turtle import  Screen
from food import Food
from scoreboard import ScoreBoard
import time
screen = Screen()
screen.setup(width=600 , height= 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) #Disables automatic screen updates. Normally, turtle graphics auto-refresh the screen after every movement, which can slow down animation or rendering.By setting screen.tracer(0), you're telling Turtle: Don't refresh the screen until I explicitly tell you to.
snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.listen()
screen.onkey(snake.up , "Up")
screen.onkey(snake.down , "Down")
screen.onkey(snake.left , "Left")
screen.onkey(snake.right , "Right")
game_is_on =True
game_score =1
while game_is_on:
    screen.update()   ##Manually refreshes the screen. You call this whenever you're ready to show updates — typically after a loop or group of turtle movements.
    time.sleep(0.1)
    snake.move_snake()
    if snake.head.distance(food) < 15:
        food.randomness()
        snake.extend()
        scoreboard.increase_score()

    if  snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() >280 or snake.head.ycor() < -280 :
        scoreboard.game_over()
        game_is_on = False

    for snake_segment in snake.segments[1:] :
        if snake.head.distance(snake_segment) < 10 :
                game_is_on = False
                scoreboard.collision_with_tail()

screen.exitonclick()