from random import randint

def schema():
    """Define the problem schema"""
    print "What type of problem do you want?"
    print "1. Add To"
    print "2. Take From"
    print "3. Put Together / Take Apart."
    print "4. Compare"
    
    #To do a while loop with a condition, you need to initialize the variables
    choice = None
    schema = ""
    while not (0 < choice < 5):
        choice = raw_input("Please type a number between 1 and 4\n> ")
        try:
            choice = int(choice)
            if choice == 1:
                schema = "add-to"
            elif choice == 2:
                schema = "take-from"
            elif choice == 3:
                schema = "put-take"
            elif choice == 4:
                schema = "compare-more"
            else:
                continue
        except ValueError:
            continue
    return schema

def unknown_one():
    """Define the unknown value for add-to and take-from schemas"""
    print "Which value is unknown?"
    print "1. Start"
    print "2. Change"
    print "3. Result"
    
    choice = None
    while not (0 < choice < 4):
        choice = raw_input("Please type a number between 1 and 3\n> ")
        try:
            choice = int(choice)
            if choice == 1:
                unknown = "start"
            elif choice == 2:
                unknown = "change"
            elif choice == 3:
                unknown = "result"
            else:
                continue
        except ValueError:
            continue
    return unknown

def unknown_two():
    """Define the unknown value for put-take schema"""
    print "Which value is unknown?"
    print "1. One addend"
    print "2. Total"
    print "3. Both addends"
    
    choice = None
    while not (0 < choice < 4):
        choice = raw_input("Please type a number between 1 and 3\n> ")
        try:
            choice = int(choice)
            if choice == 1:
                unknown = "one"
            elif choice == 2:
                unknown = "total"
            elif choice == 3:
                unknown = "both"
            else:
                continue
        except ValueError:
            continue
    return unknown

def unknown_three():
    """Define the unknown value for compare-more schema"""
    print "Which value is unknown?"
    print "1. Difference"
    print "2. Larger quantity"
    print "3. Smaller quantity"
    
    choice = None
    while not (0 < choice < 4):
        choice = raw_input("Please type a number between 1 and 3\n> ")
        try:
            choice = int(choice)
            if choice == 1:
                unknown = "difference"
            elif choice == 2:
                unknown = "larger"
            elif choice == 3:
                unknown = "smaller"
            else:
                continue
        except ValueError:
            continue
    return unknown

def range():
    """Define the number range"""
    print "Choose a difficulty level"
    print "1. Sums less than 10"
    print "2. Sums less than 20"
    print "3. Sums less than 100"
    
    choice = None
    while not (0 < choice < 4):
        choice = raw_input("Please type a number between 1 and 3\n> ")
        try:
            choice = int(choice)
        except ValueError:
            continue
    return choice

def enter_name():
    """Get the gender and name"""
    print "Should the problem feature a boy or a girl?"
    
    choice = None
    while not(choice == 'boy' or choice == 'girl'):
        choice = raw_input("Please type 'boy' or 'girl'\n> ")
        if choice == "boy":
            gend = choice
            print "What should his name be?"
            nme = raw_input("> ")
        elif choice == "girl":
            gend = choice
            print "What should her name be?"
            nme = raw_input("> ")
        else:
            continue
    return (gend, nme)

def input():
    """Run the input scripts"""
    print "Welcome to the word problem generator."
    sch = schema()
    
    if sch == "compare-more":
        unk = unknown_three()
    elif sch == "put-take":
        unk = unknown_two()
    else:
        unk = unknown_one()
    
    rng = range()
    x, y, z = numbers(rng)
    
    gender, name = enter_name()
    return sch, unk, x, y, z, gender, name
    
def numbers(range):
    if range == 1:
        z = randint(4, 10)
        x = randint(1, z)
        y = z - x
        return x, y, z
    elif range ==2:
        z = randint(11, 20)
        x = randint(4, z)
        y = z - x
        return x, y, z
    else:
        z = randint(21, 100)
        x = randint(6, z)
        y = z - x
        return x, y, z
