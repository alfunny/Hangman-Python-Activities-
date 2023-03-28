import turtle as t
import colorgram as col
from random import choice, randint

# Extract the colors from image

# rgb_colors = []

# colors = col.extract('hirst.jpg', 25)

# for object in colors:
#     r = object.rgb.r
#     g = object.rgb.g
#     b = object.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)


# print(rgb_colors)

color_list = [(229, 228, 226), (225, 223, 225), (199, 175, 117), (212, 222, 215), (125, 36, 24), (223, 224, 228), (167, 106, 56), (186, 159, 52), (6, 57, 83), (108, 68, 85), (112, 161, 175), (21, 122, 174), (63,
                                                                                                                                                                                                                153, 138), (39, 36, 35), (76, 40, 48), (9, 68, 47), (90, 141, 52), (182, 96, 79), (131, 38, 41), (141, 171, 156), (210, 200, 149), (179, 201, 186), (173, 153, 159), (212, 183, 176), (151, 114, 119)]
timmy = t.Turtle()
t.colormode(255)
timmy.shape("circle")
timmy.hideturtle()
timmy.speed(10)


def random_color():
    color = choice(color_list)
    return color


timmy.penup()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

for i in range(10):
    for j in range(10):
        timmy.penup()
        timmy.dot(20, random_color())
        timmy.forward(50)
    if i % 2 == 0:
        timmy.left(90)
        timmy.forward(50)
        timmy.left(90)
        timmy.forward(50)
    else:
        timmy.right(90)
        timmy.forward(50)
        timmy.right(90)
        timmy.forward(50)


sc = t.Screen()
sc.exitonclick()
