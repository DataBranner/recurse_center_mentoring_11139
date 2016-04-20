import sqlite3

def connect_db():
    """Connects to or creates a db and returns a cursor"""
    conn = sqlite3.connect('word_problems.db')
    return conn.cursor()

def make_table(c, table_name, columns):
    tables = c.execute('''SELECT name FROM sqlite_master 
                          WHERE type='table' AND name=?;''', (table_name,))
    tables = tables.fetchall()
    if not tables:
        c.execute('CREATE TABLE {} {}'.format(table_name, columns))
    else:
        print "Table name already exists"
        exit()

def delete_table(c, table_name):
    tables = c.execute('''SELECT name FROM sqlite_master 
                          WHERE type='table' AND name=?;''', (table_name,))
    tables = tables.fetchall()
    if tables:
        c.execute('DROP TABLE {}'.format(table_name))

def fill_table(c, file_name):
    """Reads .tsv file, populates db table where columns 1 & 4 are int"""
    with open(file_name, 'rU') as f:
        for record in f.read().split('\n')[1:]:
            if record:
                record = record.split('\t')
                record[0] = float(record[0])
                record[3] = float(record[3])
                c.execute('''INSERT INTO problems VALUES (?,?,?,?,?,?,?,?,?)''', 
                          record)

def print_table(c, table_name):
    for row in c.execute('SELECT * FROM {}'.format(table_name)):
        print row

