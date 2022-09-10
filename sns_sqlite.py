import re, sqlite3, os
BASE_DIR = os.path.dirname(__file__)
DATA_FILE = BASE_DIR + "/data/sns.sqlite3"

def open_db():
    conn = sqlite3.connect(DATA_FILE)
    conn.row_factory = dict_factory 
    return conn

def dict_factory(curser, row):
    d = {}
    for idx, col in enumerate(curser.description):
        d[col[0]] = row[idx]
    return d

def exec(sql, *args):
    print(args)
    db = open_db()
    c = db.cursor()
    c.execute(sql, args)
    db.commit()
    return c.lastrowid

def select(sql, *args):
    db = open_db()
    c = db.cursor()
    c.execute(sql, args)
    return c.fetchall()