
SELECT * FROM users;

INSERT INTO users (username, password) VALUES ('john.doe@gmail.com', '123456');

UPDATE users SET password='admin123' WHERE username='john.doe@gmail.com';

DELETE FROM users WHERE username = 'john.doe@gmail.com';