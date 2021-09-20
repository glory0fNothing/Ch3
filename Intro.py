def test_average(): #program 1
    #test average accepts no arguments
    #it gets the scores of three tests
    #It displays the average of the tests
    
    #Get the scores of the first, second, and third tests
    first = int(input('Enter the first score:'))
    second = int(input('Enter the second score:'))
    third = int(input('Enter the third score:'))
    
    #Calculate the average score
    total_score = first + second + third
    average = total_score / 3
    
    #Display the average score
    print('The average score is:', format(average, '.2f'))
    if average > 95:
        print('Congratulations!')
        print('That is a high score!')
        
def auto_repair_payroll(): #program 2
    #auto repair payroll accepts no arguments
    #it prompts for the hours worked and hourly pay rate
    #if > 40hrs the gross pay is 1.5x the usual
    #it displays the gross pay
    
    #Set the constant overtime pay multiple at 1.5
    OVERTIME = 1.5
    MIN_HR = 40
    
    #Get the hours worked and hourly pay rate
    hours = int(input('Enter the number of hours worked:'))
    rate = int(input('Enter the hourly pay rate:'))
    
    #Calculate and display the gross pay
    if hours > MIN_HR:
        overPay = hours * (rate * OVERTIME)
        print('Your gross pay is $',
          format(overPay, ',.2f'),
          sep='')
    else:
        grossPay = hours * rate
        print('Your gross pay is $',
          format(grossPay, ',.2f'),
          sep='')
        
def password_verifier(): #program 3
    #password verifier accepts no arguments
    #it asks for the password
    #and accepts if the password matches
    #or denies if the password is incorrect
    
    #Set the password
    PASSWORD = str('prospero')
    
    #Get the password
    enteredPassword = input('Please enter the password:')
    
    #Display if the password is correct
    if enteredPassword == PASSWORD:
        print('Password accepted.')
    else:
        print('Password is invalid')
        
def sort_names(): #Program 4
    #sort names accepts no arguments
    #it collects two full names
    #it displays them in alphabetical order
    
    #Get the two names with last name first
    name1 = input('Enter the first name (last, first):')
    name2 = input('Enter the second name (last, first):')
    
    #Display the names in alphabetical order
    print('Here are the names, sorted alphabetically.')
    
    if name1 < name2:
        print(name1)
        print(name2)
    else:
        print(name2)
        print(name1)
        
def loan_qualifier(): #Program 5
    #loan qualifier accepts no arguments
    #it gets the annual salary and years at the job
    #it calculates and displays the minimum salary
    
    MIN_SALARY = 30000
    
    #Get the annual salary and years concurred
    salary = int(input('Enter your annual salary:'))
    years = int(input('Enter the number of years at your current job:'))
    
    #Determine if qualifies and display
    if salary >= MIN_SALARY:
        if years >= 2:
            print('You qualify for the loan.')
        else:
            print('You must have been on your current job for at least two years to qualify.')
    else:
        print('You must earn at least $', format(MIN_SALARY, ',.2f'))
        
def grader(): #Program 6
    #grader accepts no arguments
    #it gets the test score
    #it tests and displays the letter grade
    
    #Get the test score
    score = int(input('Enter your test grade:'))
    
    #Test and display the letter grade
    
    if score >= 90:
        print('Your grade is A.')
    else:
        if score >= 80:
            print('Your grade is B.')
        else:
            if score >= 70:
                print('Your grade is C.')
            else:
                if score >= 60:
                    print('Your grade is D.')
                else:
                    print('Your grade is F.')
        
def grader_v2(): #Program 6 v2
    #grader v2 accepts no arguments
    #it gets the test score
    #it tests and displays the letter grade
    
    #Get the test score
    score = int(input('Enter your test grade:'))
    
    #Test and display the letter grade
    
    if score >= 90:
        print('Your grade is A.')
    elif score >= 80:
        print('Your grade is B.')
    elif score >= 70:
        print('Your grade is C.')
    elif score >= 60:
        print('Your grade is D.')
    else:
        print('Your grade is F.')
        
def loan_qualifier_v2(): #Program 7
    #loan qualifier v2 accepts no arguments
    #it gets the annual salary and years at the job
    #it calculates and displays the minimum salary
    
    MIN_SALARY = 30000
    
    #Get the annual salary and years concurred
    salary = int(input('Enter your annual salary:'))
    years = int(input('Enter the number of years at your current job:'))
    
    #Determine if qualifies and display
    if salary >= MIN_SALARY and years >= 2:
        print('You qualify for the loan.')
    else:
        print('You do not qualify for the loan.')
    
def loan_qualifier_v3(): #Program 8
    #loan qualifier v2 accepts no arguments
    #it gets the annual salary and years at the job
    #it calculates and displays the minimum salary
    
    MIN_SALARY = 30000
    
    #Get the annual salary and years concurred
    salary = int(input('Enter your annual salary:'))
    years = int(input('Enter the number of years at your current job:'))
    
    #Determine if qualifies and display
    if salary >= MIN_SALARY or years >= 2:
        print('You qualify for the loan.')
    else:
        print('You do not qualify for the loan.')
        
#SPOTLIGHT - Hit the Target Game
    
import turtle

#Named constants
SCREEN_W = 600 
SCREEN_H = 600
TARGET_LLEFT_X = 100
TARGET_LLEFT_Y = 250
TARGET_W = 25
FORCE_FACTOR = 30 #arbitrary force factor
PROJECTILE_SPEED = 1 #animation speed
NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180

#set up the turtle window
turtle.setup(SCREEN_W, SCREEN_H)

#Draw the target
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_W)
turtle.setheading(NORTH)
turtle.forward(TARGET_W)
turtle.setheading(WEST)
turtle.forward(TARGET_W)
turtle.setheading(SOUTH)
turtle.forward(TARGET_W)
turtle.penup()

#Hit the target

if turtle.xcor() != 0 and turtle.ycor() != 0:
    turtle.goto(0, 0)

if not(turtle.isdown()):
    turtle.pendown()

turtle.showturtle()

turtle.setheading(65)

turtle.forward(290)
