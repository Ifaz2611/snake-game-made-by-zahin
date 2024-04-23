import turtle
import time
import random

delay = 0.1

#Score 
score = 0
high_score = 0

### setup screen ###
wn = turtle.Screen()
wn.title("*** Python Snake Game // Ifaz md zahin ***")
wn.bgcolor("black")
wn.setup(width= 600, height = 600)
wn.tracer(0) ##Turns of screen updates

### Snake ### 
head = turtle.Turtle()
head.speed(0)
head.shape("square") 
head.color("white", "red")
head.penup()
head.goto(0,0)
head.direction = "stop"

### Shake Food ###
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("yellow", "green")
food.penup()
food.goto(0,100)

segments = []

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score: 0  || HighScore: 0", align= "center", font= ("Courier", 14,"normal"))

### Functions ###

def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"


def player_move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


### Keyboard Bindings ###
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

### Main Game Loop ###
while True:
    wn.update()

    # Check for a collision with the border
    if head.xcor()> 290 or head.xcor()<-290 or head.ycor()> 290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        #Hide the Segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear Segments list
        segments.clear()
        score = 0

        pen.clear()
        pen.write("Score: {} || HighScore: {}".format(score, high_score), align= "center", font= ("Courier", 14,"normal"))




    # Check for a collision with the food
    if head.distance(food) < 20:
        #move the food to a random position
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        #Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        segments.append(new_segment)

        # Increase the Score
        score = score + 1

        if score > high_score:
            high_score = score
            
        pen.clear()
        pen.write("Score: {} || HighScore: {}".format(score, high_score), align= "center", font= ("Courier", 14,"normal"))

    #moves the end segments first
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    #move segment 0 to where head is

    if len (segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
    

    player_move()

    # Check for head collision with the body

    for segment in segments:
        if segment.distance(head)< 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            #hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            #clear segments list
            segments.clear()

            # Reset the score 
            

    time.sleep(delay)


wn.mainloop()
