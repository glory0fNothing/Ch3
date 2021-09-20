def day_converter(): #Exercise 1
    #day converter accepts no arguments
    #it gets the number of the day range
    #it displays the day of the week in Spanish
    
    #Set the day constants
    MON = 1
    TUE = 2
    WED = 3
    THU = 4
    FRI = 5
    SAT = 6
    SUN = 7
    
    SP_MON = 'Lunes'
    SP_TUE = 'Martes'
    SP_WED = 'Miercoles'
    SP_THU = 'Jueves'
    SP_FRI = 'Viernes'
    SP_SAT = 'Sabado'
    SP_SUN = 'Domingo'
    
    #Get the day number
    dayNumber = int(input('Enter a number in the range 1 through 7 (Monday to Sunday):'))
    
    #Determine and display the day in Spanish
    
    if dayNumber == MON:
        print(SP_MON)
    elif dayNumber == TUE:
        print(SP_TUE)
    elif dayNumber == WED:
        print(SP_WED)
    elif dayNumber == THU:
        print(SP_THU)
    elif dayNumber == FRI:
        print(SP_FRI)
    elif dayNumber == SAT:
        print(SP_SAT)
    elif dayNumber == SUN:
        print(SP_SUN)
    else:
        print('Error')

def roman_numerals(): #Exercise 4
    #roman numerals accepts no arguments
    #it gets a number 1 through 10
    #It displays that number in roman numeral form
    
    #Set the number constants
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    
    RO_ONE = 'I'
    RO_TWO = 'II'
    RO_THREE = 'III'
    RO_FOUR = 'IV'
    RO_FIVE = 'V'
    RO_SIX = 'VI'
    RO_SEVEN = 'VII'
    RO_EIGHT = 'VIII'
    RO_NINE = 'IX'
    RO_TEN = 'X'
    
    #Get the number
    number = int(input('Enter a number from 1 through 10:'))
    
    #Decide and display the number a roman numeral
    
    if number == ONE:
        print(RO_ONE)
    elif number == TWO:
        print(RO_TWO)
    elif number == THREE:
        print(RO_THREE)
    elif number == FOUR:
        print(RO_FOUR)
    elif number == FIVE:
        print(RO_FIVE)
    elif number == SIX:
        print(RO_SIX)
    elif number == SEVEN:
        print(RO_SEVEN)
    elif number == EIGHT:
        print(RO_EIGHT)
    elif number == NINE:
        print(RO_NINE)
    elif number == TEN:
        print(RO_TEN)
    else:
        print('Error')
        
def color_mixer(): #Exercise 7
    #color mixer accepts no arguments
    #it gets the primary colors
    #it mixes and displays the new color
    
    #Set the color constants
    RED = 'red'
    BLUE = 'blue'
    YELLOW = 'yellow'
    PURPLE = 'Purple'
    ORANGE = 'Orange'
    GREEN = 'Green'
    
    #Get the colors
    color1 = input('Enter the first primary color:').lower()
    color2 = input('Enter the second primary color:').lower()
    
    #Set an error message for any non-primary color inputs
    if (color1 != RED or BLUE or YELLOW) or (color2 != RED or BLUE or YELLOW):
        print('ERROR: Please enter valid primary colors.')
    else:
        #Combine and display the new color
    
        if (color1 == RED and color2 == BLUE) or (color1 == BLUE and color2 == RED):
            print('Your mixed color is:', PURPLE)
        elif (color1 == RED and color2 == YELLOW) or (color1 == YELLOW and color2 == RED):
            print('Your mixed color is:', ORANGE)
        elif (color1 == YELLOW and color2 == BLUE) or (color1 == BLUE and color2 == YELLOW):
            print('Your mixed color is:', GREEN)
            
def hotDog(): #Exercise 8
    #hot Dog accepts no arguments
    #it gets the number of people and allowed hotdogs
    #it displays the needed packages and leftover dogs and buns
    
    #Set the constants per package of hotdogs and buns
    dogPackage = 10
    bunPackage = 8
    
    #Get the number of people and maximum allowed dogs per person
    people = int(input('How many people are coming to the cookout? '))
    maxDogs = int(input('How many hotdogs are each person allowed to eat? '))
    TOTALDOG = people * maxDogs
    #Calculate the number of required packages of hotdogs and buns
    if not float(TOTALDOG / dogPackage).is_integer():
        dogNeed = (TOTALDOG // dogPackage) + 1
    else:
        dogNeed = TOTALDOG // dogPackage
    
    if not float(TOTALDOG / bunPackage).is_integer():
        bunNeed = (TOTALDOG // bunPackage) + 1
    else:
        bunNeed = TOTALDOG // bunPackage

    dogRemain = dogNeed * 10 - TOTALDOG
    bunRemain = bunNeed * 8 - TOTALDOG
    
    #Display the number of required hotdogs and buns
    print('The minimum number of packages of hotdogs required:', dogNeed)
    print('The minimum number of packets of hotdog buns required:', bunNeed)
    print('The number of hotdogs left over:', dogRemain)
    print('The number of hotdog buns left over:', bunRemain)

def timeCalculator(): #Exercise 15
    #time Calculator accepts no arguments
    #it gets an amount of time in seconds
    #it displays the time separated into seconds, minutes, and hours
    
    #Set the amounts of time as constants
    MINUTE = 60
    HOUR = 3600
    DAY = 86400
    
    #Get the amount of time from the user
    time = int(input('Enter an amount of time in seconds: '))
    
    #Calculate the time in hours, minutes, and seconds
    if time >= MINUTE and time <= HOUR:
        minutes = time // MINUTE
        seconds = time % MINUTE
    elif time >= HOUR and time <= DAY:
        hours = time // HOUR
        minutes = (time % HOUR) // MINUTE
        seconds = (time % HOUR) % MINUTE
    else:
        days = time // DAY
        hours = (time % DAY) // HOUR
        minutes = ((time % DAY) % HOUR) // MINUTE
        seconds = ((time % DAY) % HOUR) % MINUTE
        
    #Display the amount of time in hours, minutes, and seconds
    
    if time >= MINUTE and time <= HOUR:
        print(time, 'seconds is', minutes, 'minute(s) and', seconds, 'second(s)')
    elif time >= HOUR and time <= DAY:
        print(time, 'seconds is', hours, 'hour(s),', minutes, 'minute(s), and', seconds, 'second(s)')
    else:
        print(time, 'seconds is', days, 'day(s),', hours, 'hour(s),', minutes, 'minute(s), and', seconds, 'second(s)')
        
def leapYear(): #Exercise 16
    #leap Year accepts no arguments
    #it gets a year from the user
    #it diplays if that year is a leap year
    #and how many days are in February that year
    
    #Set year constants
    CEN = 100
    FOURCEN = 400
    FOURYEAR = 4
    
    #Get the year from the user
    year = int(input('Enter a year: '))
    
    #Calculate and display if it is a leap year and the days of February
    if float(year / CEN).is_integer() and float(year / FOURCEN).is_integer():
        print(year, 'is a leap year. There are 29 days in the month of February.')
    elif not float(year / CEN,).is_integer() and float(year / FOURYEAR).is_integer():
        print(year, 'is a leap year. There are 29 days in the month of February.')
    else:
        print(year, 'is not a leap year. There are 28 days in the month of February.')
        
def sirFixAlot(): #Exercise 17
    #sir Fix Alot accepts no arguments
    #it prompts if the internet is working
    #it displays possible troubleshooting
    
    CORRECT = 'Netflix and Chill'
    FIXED = 'Did that fix the problem? (Yes/No) '
    
    print('Reboot computer and try to connect')
    print()
    
    answer = input(FIXED)
    
    if answer.lower() == 'yes':
        print()
        print(CORRECT)
    else:
        print()
        print('Reboot router and try to connect')
        print()
        answer2 = input(FIXED)
        if answer2.lower() == 'yes':
            print()
            print(CORRECT)
        else:
            print()
            print('Verify cables are firmly attached')
            print()
            answer3 = input(FIXED)
            if answer3.lower() == 'yes':
                print()
                print(CORRECT)
            else:
                print()
                print('Move router to better location')
                print()
                answer4 = input(FIXED)
                if answer4.lower() == 'yes':
                    print()
                    print(CORRECT)
                else:
                    print()
                    print('Get a new router')
                    
def canWeJustEat(): #Exercise 18
    #can We Just Eat accepts no arguments
    #it prompts for vegetarians, vegans, or gluten intolerance
    #it displays restaurant choices
    
    #Joe’s Gourmet Burgers - no no no
    #Main Street Pizza Company - yes no yes
    #Corner Café - yes yes yes
    #Mama's Fine Italian -  yes no no
    #The Chef’s Kitchen - yes yes yes
    
    choices = 'Here are your restaurant choices: '
    
    veg = input('Is anyone in your party a vegetarian? ')
    vegan = input('Is anyone in your party a vegan? ')
    gluten = input('Does anyone in your party have a gluten intolerance? ')
    
    if (veg.lower() == 'yes' and vegan.lower() == 'yes' and gluten.lower() == 'yes') \
       or (veg.lower() == 'yes' and vegan.lower() == 'yes' and gluten.lower() == 'no') \
       or (veg.lower() == 'no' and vegan.lower() == 'yes' and gluten.lower() == 'no') \
       or (veg.lower() == 'no' and vegan.lower() == 'yes' and gluten.lower() == 'yes'):
        print(choices)
        print('Corner Café')
        print("The Chef's Kitchen")
    elif veg.lower() == 'yes' and vegan.lower() == 'no' and gluten.lower() == 'no':
        print(choices)
        print('Main Street Pizza Company')
        print('Corner Café')
        print("Mama's Fine Italian")
        print("The Chef's Kitchen")
    elif veg.lower() == 'no' and vegan.lower() == 'no' and gluten.lower() == 'no':
        print(choices)
        print("Joe's Gourmet Burgers")
        print('Main Street Pizza Company')
        print('Corner Café')
        print("Mama's Fine Italian")
        print("The Chef's Kitchen")
    elif (veg.lower() == 'no' and vegan.lower() == 'no' and gluten.lower() == 'yes') \
         or (veg.lower() == 'yes' and vegan.lower() == 'no' and gluten.lower() == 'yes'):
        print(choices)
        print('Main Street Pizza Company')
        print('Corner Café')
        print("The Chef's Kitchen")
    
def hitTheTarget(): #Exercise 19
    #hit The Target accepts no arguments
    
    
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

    #Set up to hit the target

    if turtle.xcor() != 0 and turtle.ycor() != 0:
        turtle.goto(0, 0)

    if not(turtle.isdown()):
        turtle.pendown()

    turtle.showturtle()

    #Get the angle and distance for the turtle to travel
    
    angle = int(input('Enter an angle for the turtle to travel: '))
    force = int(input('Enter the force factor for the turtle: '))
    distance = force * FORCE_FACTOR
    
    turtle.setheading(angle)

    turtle.forward(distance)

    #Did it hit?
    if (turtle.xcor() >= TARGET_LLEFT_X and
        turtle.xcor() <= (TARGET_LLEFT_X + TARGET_W) and
        turtle.ycor() >= TARGET_LLEFT_Y and
        turtle.ycor() <= (TARGET_LLEFT_Y + TARGET_W)):
            print('Target hit!')
    else:
        print('You missed the target')