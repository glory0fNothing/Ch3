def repeating_squares(): #16
    #repeating squares accepts no arguments
    #it gets the number of squares to draw
    #and displays that number of squares connected together
    
    #Set the base square size
    BASE_SQ = 10
    SQ_SPACING = 5
    CHANGE = 90
    
    #Get the number of squares from the user
    squares = int(input('Enter the number of squares: '))
    
    #Set up the turtle
    import turtle
    turtle.hideturtle()
    turtle.speed(0)
    turtle.penup()
    turtle.goto(100, 0)
    turtle.pendown()
    
    #Validate that the number of squares inputted is a positive number
#     while squares < 0:
#         print('ERROR: Please enter a positive number of squares')
#         squares = int(input('Enter the number of squares: '))
#     
#     #Draw the squares
#     for num in range(1, squares + 1):
#         turtle.forward(BASE_SQ)
#         turtle.left(CHANGE)
#         turtle.forward(BASE_SQ)
#         turtle.left(CHANGE)
#         
#         BASE_SQ += SQ_SPACING
    turtle.forward(BASE_SQ)