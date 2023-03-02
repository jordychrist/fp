-- CREATE TABLE transactions (
-- id INTEGER PRIMARY KEY AUTOINCREMENT,
-- user_id INTEGER NOT NULL,
-- name TEXT NOT NULL,
-- shares INTEGER NOT NULL,
-- price NUMERIC NOT NULL,
-- type TEXT NOT NULL,
-- symbol TEXT NOT NULL,
-- time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
-- FOREIGN KEY(user_id) REFERENCES users(id)
-- );

-- CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT NOT NULL,
--  hash TEXT NOT NULL, cash NUMERIC NOT NULL DEFAULT 10000.00);
-- CREATE UNIQUE INDEX username ON users (username);

-- ALTER TABLE users ADD email TEXT NULL;

-- SELECT name, user_id, qty FROM events WHERE name = "burning man";
SELECT * FROM users;

-- DELETE FROM users WHERE id= 8;
-- CREATE TABLE events (
-- id INTEGER PRIMARY KEY AUTOINCREMENT,
-- user_id INTEGER NOT NULL,
-- name TEXT NOT NULL,
-- date TEXT NOT NULL,
-- location TEXT NOT NULL,
-- price TEXT NOT NULL,
-- image TEXT NULL,
-- time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
-- FOREIGN KEY(user_id) REFERENCES users(id)
-- );

-- CREATE TABLE pending (
-- id INTEGER PRIMARY KEY AUTOINCREMENT,
-- name TEXT NOT NULL,
-- date TEXT NOT NULL,
-- time TEXT NOT NULL,
-- location TEXT NOT NULL,
-- price TEXT NOT NULL,
-- image TEXT NULL
-- );

-- CREATE TABLE slush (
-- id INTEGER PRIMARY KEY AUTOINCREMENT,
-- name TEXT NULL,
-- qty TEXT NULL
-- );

--   Add to the pending events database
-- INSERT INTO pending (
-- name, date, time, location, price)
-- VALUES
-- ('edc', '5/19/23', '17:00', 'Las Vegas', '390');


-- UPDATE pending
-- SET name = 'burning man'
-- WHERE id = 1;

-- ALTER TABLE events
-- ADD qty TEXT NOT NULL;