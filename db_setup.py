import sqlite3

def connect_db():
    """Connects to or creates a db and returns a cursor"""
    conn = sqlite3.connect('word_problems.db')
    c = conn.cursor()
    return c

def make_table(c, table_name, columns):
    c.execute('CREATE TABLE {} {}'.format(table_name, columns))

def delete_table(c, table_name):
    c.execute('DROP TABLE {}'.format(table_name))

def fill_table(c, file_name):
    """Reads a .tsv file and fills a db table where the 1st and 4th columns are int"""
    with open(file_name, 'rU') as f:
        for record in f.read().split('\n')[1:]:
            if record:
                record = record.split('\t')
                record[0] = float(record[0])
                record[3] = float(record[3])
                c.execute('''INSERT INTO problems VALUES (?,?,?,?,?,?,?,?,?)''', record)

def print_table(c, table_name):
    for row in c.execute('SELECT * FROM {}'.format(table_name)):
        print row

