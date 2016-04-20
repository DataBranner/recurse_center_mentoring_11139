from random import randint

def schema():
    """Define the problem schema"""
    #To do a while loop with a condition, you need to initialize the variables
    choice = None
    choice_to_return = {1: ('add-to', 'Add To'), 
                          2: ('take-from', 'Take From'), 
                          3: ('put-take', 'Put Together / Take Apart'),
                          4: ('compare-more', 'Compare')}
    print "What type of problem do you want?"
    for key, value in choice_to_return.items():
        print '{}. {}'.format(key, value[1])

    while choice not in choice_to_return:
        choice = raw_input("Please type a number between 1 and 4\n> ")
        try:
            choice = int(choice)
        except ValueError:
            continue
    return choice_to_return[choice][0]

def unknown_one():
    """Define the unknown value for add-to and take-from schemas"""
    choice = None
    choice_to_return = {1: ('start', 'Start'), 
                        2: ('change', 'Change'), 
                        3: ('result', 'Result')}
    print "Which value is unknown?"
    for key, value in choice_to_return.items():
        print '{}. {}'.format(key, value[1])

    while choice not in choice_to_return:
        choice = raw_input("Please type a number between 1 and 3\n> ")
        try:
            choice = int(choice)
        except ValueError:
            continue
    return choice_to_return[choice][0]

def unknown_two():
    """Define the unknown value for put-take schema"""
    choice = None
    choice_to_return = {1: ('one', 'One addend'), 
                        2: ('total', 'Total'), 
                        3: ('both', 'Both addends')}
    print "Which value is unknown?"
    for key, value in choice_to_return.items():
        print '{}. {}'.format(key, value[1])

    while choice not in choice_to_return:
        choice = raw_input("Please type a number between 1 and 3\n> ")
        try:
            choice = int(choice)
        except ValueError:
            continue
    return choice_to_return[choice][0]

def unknown_three():
    """Define the unknown value for compare-more schema"""
    choice = None
    choice_to_return = {1: ('difference', 'Difference'), 
                        2: ('larger', 'Larger quantity'), 
                        3: ('smaller', 'Smaller quantity')}
    print "Which value is unknown?"
    for key, value in choice_to_return.items():
        print '{}. {}'.format(key, value[1])

    while choice not in choice_to_return:
        choice = raw_input("Please type a number between 1 and 3\n> ")
        try:
            choice = int(choice)
        except ValueError:
            continue
    return choice_to_return[choice][0]

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
    while not (choice == 'boy' or choice == 'girl'):
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
