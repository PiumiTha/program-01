import turtle
import datetime
import math

#Function add clock make more attractive(Question number 02)
def hearta(k):
    return 15 * math.sin(k) ** 3

def heartb(k):
    return 12 * math.cos(k) - 4 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

# Create a turtle screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("SLTC-BAIT Batch1 Clock")
screen.tracer(1)  

def draw_heart():
    turtle.speed(1100)  
    turtle.color("red")  
    
    for i in range(360):
        turtle.goto(hearta(i) * 20, heartb(i) * 20)
    turtle.end_fill()  
    turtle.penup()
    turtle.goto(0, 0)


draw_heart()

# Function to get the local time without importing pytz (Question number 01)
def get_local_time(timezone_offset):
    utc_now = datetime.datetime.utcnow()
    local_now = utc_now + datetime.timedelta(hours=timezone_offset)
    return local_now

timezone_offset = 5.5

# Clock setup
face = turtle.Turtle()
face.shape("circle")
face.color("yellow")
face.fillcolor("gold")
face.shapesize(stretch_wid=2, stretch_len=2)
face.penup()

hour_hand = turtle.Turtle()
hour_hand.shape("arrow")
hour_hand.shapesize(stretch_wid=0.6, stretch_len=6)
hour_hand.color("white")

minute_hand = turtle.Turtle()
minute_hand.shape("arrow")
minute_hand.shapesize(stretch_wid=0.6, stretch_len=12)
minute_hand.color("white")

second_hand = turtle.Turtle()
second_hand.shape("arrow")
second_hand.shapesize(stretch_wid=0.4, stretch_len=14)
second_hand.color("orange")

digital_display = turtle.Turtle()
digital_display.hideturtle()
digital_display.penup()
digital_display.color("orange")
digital_display.goto(0, -100)
digital_display.write("", align="center", font=("Arial", 12, "normal"))

def draw_hour_labels():
    hour_labels = turtle.Turtle()
    hour_labels.color("white")
    hour_labels.penup()
    hour_labels.hideturtle()
    numerals = ["IX", "X", "XI", "XII", "I", "II", "III", "IV", "V", "VI", "VII", "VIII"]
    for i in range(12):
        angle = math.radians(30 * i - 90)
        label_x = 150 * math.sin(angle)
        label_y = 150 * math.cos(angle)
        hour_labels.goto(label_x, label_y - 40)
        hour_labels.write(numerals[i], align="center", font=("Arial", 20, "bold"))

def update_clock():
    now = get_local_time(timezone_offset)
    hour_angle = (now.hour % 12) * 30 + now.minute / 2
    minute_angle = now.minute * 6 + now.second * 0.1
    second_angle = now.second * 6

    hour_hand.setheading(90 - hour_angle)
    minute_hand.setheading(90 - minute_angle)
    second_hand.setheading(90 - second_angle)

    # Add digital time to the clock, add aditional function to clock(Question number 03)
    digital_time = now.strftime("%H:%M:%S %p")
    digital_display.clear()
    digital_display.write(digital_time, align="center", font=("Arial", 20, "normal"))

    screen.update()
    screen.ontimer(update_clock, 1000)

draw_hour_labels()
update_clock()

# Keep the window open
turtle.done()
