from sns_sqlite import exec 

# 投稿情報
exec('''
CREATE TABLE posted_senryu (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id     TEXT,
    contents    TEXT,
    create_at   TIMESTAMP DEFAULT (DATETIME('now', 'localtime'))
)
''')

exec('''
CREATE TABLE subscribers (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    subscriber  TEXT,
    author      TEXT
)
''')