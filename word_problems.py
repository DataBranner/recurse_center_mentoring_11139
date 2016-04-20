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
                schema = "add_to_"
            elif choice == 2:
                schema = "take_from_"
            elif choice == 3:
                schema = "put_take_"
            elif choice == 4:
                schema = "compare_more_"
            else:
                continue
        except ValueError:
            continue
    return schema

def unknown():
    """Define the unknown value"""
    print "Which value is unknown?"
    print "1. Start"
    print "2. Change"
    print "3. Result"
    
    choice = None
    while not (0 < choice < 4):
        choice = raw_input("Please type a number between 1 and 3\n> ")
        try:
            choice = int(choice)
        except ValueError:
            continue
    return choice

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
    unk = unknown()
    rng = range()
    gender, name = enter_name()
    return sch, unk, rng, gender, name
    
def numbers(range):
    if range == 1:
        pass
    else:
        pass

def main():
    """Run the main program"""
    schema, unk, rng, gender, name = input()
    d = {'girl': {'subj': 'she', 'obj': 'her', 'poss': 'her'},'boy': {'subj': 
    'he', 'obj': 'him', 'poss': 'his'}}
    sch_prob = schema + str(unk)
    print sch_prob
    subject = d[gender]['subj']
    object = d[gender]['obj']
    poss = d[gender]['poss']

    x = 3
    y = 5
    z = x + y
    name1 = name
    name2 = 'Helen'

    #'test: {}, {}; {}.'.format(5, "what", 9.000)
    p = {'add_to_1': {'prob': "{0} read {1} pages on Monday. {2} read {3} pages on Tuesday. How many pages did {4} read all together?", 
    'var': (name, x, subject.capitalize(), y, subject)}, 
    'add_to_2': {'prob': "{} read {} pages on Monday. {} read more pages on Tuesday, bringing {} total to {} pages read. How many pages did {} read on Tuesday?", 
    'var': (name, x, subject.capitalize(), poss, z, name)},
    'add_to_3': {'prob': "{} started a new book on Monday. On Tuesday, {} kept reading the same book and read {} more pages. {} ended up on page {}. How many pages had {} read on Monday?",
    'var': (name, subject, y, subject.capitalize(), z, name)},
    'take_from_1': {'prob': "{} had a collection of {} pencils. {} gave {} of the pencils to {} good friend. How many pencils does {} have now?",
    'var': (name, x, subject.capitalize(), y, poss, subject)},
    'take_from_2': {'prob': "{} had a collection of {} pencils. {} gave some of the pencils to {} good friend and now {} has {} pencils. How many pencils did {} give away?",
    'var': (name, x, subject.capitalize(), poss, subject, z, subject)},
    'take_from_3': {'prob': "{} had a collection of pencils. {} gave {} of the pencils to {} good friend, and now {} has {} pencils. How many pencils did {} start with?",
    'var': (name, subject.capitalize(), y, poss, subject, z, subject)},
    'put_take_1': {'prob': "{} has {} red cars and {} blue cars. How many cars does {} have all together?",
    'var': (name, x, y, subject)},
    'put_take_2': {'prob': "{} is sorting {} toy cars into two buckets. {} has {} cars. How many can {} put into each bucket?",
    'var': (name, poss, subject.capitalize(), z, subject)},
    'put_take_3': {'prob': "{} has {} toy cars. {} of them are red and the rest are blue. How many of the cars are blue?",
    'var': (name, z, x)},
    'compare_more_1': {'prob': "{} has {} carrots, and {} has {} carrots. How many more carrots does {} have?",
    'var': (name1, z, name2, x, name)},
    'compare_more_2': {'prob': "{} has {} more carrots than {}. {} has {} carrots. How many carrots does {} have?",
    'var': (name1, y, name2, name2, x, name1)},
    'compare_more_3': {'prob': "{} has {} more carrots than {}. {} has {} carrots. How many carrots does {} have?",
    'var': (name1, y, name2, name1, z, name2)}
    }
    problem = p[sch_prob]['prob']
    variable = p[sch_prob]['var']
    print problem.format(*variable)

if __name__ == '__main__':
    main()