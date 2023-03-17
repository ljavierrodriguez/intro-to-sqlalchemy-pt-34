

# INSERT INTO users (username, password) VALUES ('john.doe@gmail.com', '123456');

user = User()
user.username = "john.doe@gmail.com"
user.password = "123456"

db.session.add(user) 
db.session.commit()

# SELECT * FROM users;

users = User.query.all() # SELECT * FROM users;

user = User.query.filter_by(username="john.doe@gmail.com").first()  # <User 1> # SELECT * FROM users WHERE username="john.doe@gmail.com" LIMIT 1

user = User.query.get(1) # SELECT * FROM users WHERE id = 1;

# UPDATE users SET password='admin123' WHERE username='john.doe@gmail.com';

user = User.query.get(1) # SELECT * FROM users WHERE id = 1;
user.username = "jane.doe@gmail.com"
user.password = "4DaM1n123"
db.session.commit()


# DELETE FROM users WHERE username = 'john.doe@gmail.com';

user = User.query.get(1)
db.session.delete(user)
db.session.commit()
