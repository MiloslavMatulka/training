from turtle import speed, shape, forward, left, exitonclick

speed(10)
shape("arrow")

for number in range(10):
    
    side = 25
    diag = side * (2 ** (1 / 2))
    roof = (side * (2 ** (1 / 2))) / 2

    # Square
    for i in range(4):
        forward(side)
        left(90)

    # Diagonals and a roof
    #
    # Diagonal 1
    left(45)
    forward(diag)

    # Roof
    for r in range(2):
        left(90)
        forward(roof)

    # Diagonal 2
    left(90)
    forward(diag)

    # Space between houses
    left(45)
    forward(10)

exitonclick()
