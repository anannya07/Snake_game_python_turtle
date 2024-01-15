from turtle import Turtle,Screen
from snake import Snake
from food import Food
from score import ScoreBoard
import time
start = [(0,0) ,(-20,0) , (-40,0)]
segments = []
screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)



snake = Snake()
food =Food()
score=ScoreBoard()



screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


    #detection collision between food and snake and boom!!!!!!!!!!!!!

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    #detect collision with wall

    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 :
        game_is_on = False
        score.game_over()


screen.exitonclick()