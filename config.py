# SQLlite
db_name = 'db'

CREATE_TABLES = """ CREATE TABLE IF NOT EXISTS users (
                            id TEXT PRIMARY KEY,
                            username TEXT,
                            date_banned DATETIME,
                            banned_item TEXT
                        ); """

INSERT_RECORD = """ INSERT INTO users VALUES (?, ?, ?, ?); """

DELETE_RECORD = """ DELETE FROM users WHERE id = ? """

FIND_RECORD = """ SELECT COUNT(*) FROM users WHERE id = ? """

# PRAW
bot_name = 'Main'
subreddit = 'All'