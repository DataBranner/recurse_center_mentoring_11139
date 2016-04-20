import sqlite3
import problem_setup
import db_setup
from random import randint


def main():
    c = db_setup.connect_db()
    file_name = 'problems.tsv'
    table_name = 'problems'
    columns = '''(row_id int, problem text, variables text, var_count int, equation text, 
    solution text, operation text, schema text, unknown text)'''

    db_setup.delete_table(c, table_name)
    db_setup.make_table(c, table_name, columns)
    db_setup.fill_table(c, file_name)
#    db_setup.print_table(c, table_name)

    schema, unk, x, y, z, gender, name = problem_setup.input()
    d = {'girl': {'subj': 'she', 'obj': 'her', 'poss': 'her'},'boy': {'subj': 
    'he', 'obj': 'him', 'poss': 'his'}}
    subject = d[gender]['subj']
    object = d[gender]['obj']
    poss = d[gender]['poss']
    
    name1 = name
    name2 = 'Helen'
    
    c.execute('''SELECT problem FROM {} WHERE schema = "{}" AND unknown = "{}" 
    LIMIT 1'''.format(table_name, schema, unk))
    prob = c.fetchall()
    problem = str(prob)[:-4][4:]
    
    c.execute('''SELECT variables FROM {} WHERE schema = "{}" AND unknown = "{}" 
    LIMIT 1'''.format(table_name, schema, unk))
    var = c.fetchall()
    var = str(var)[:-6][6:]
    variable = eval(var)
    
    print problem.format(*variable)


if __name__ == '__main__':
    main()
