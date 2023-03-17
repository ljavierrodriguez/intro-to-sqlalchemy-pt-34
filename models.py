class User:
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(120), unique=True, nullable=False)
    password = Column(String(120), nullable=False)
    posts = relationship('Post', backref='user')

class Role:
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)

class Profile:
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key=True)

class Post:
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(200), unique=True, nullable=False)
    date = Column(DateTime(), nullable=False)
    published = Column(Boolean(), nullable=False, default=False)
    users_id = Column(Integer, ForeignKey('users.id'), nullable=False)




""" 

[] = map(lambda, list)

[] = list.map(function)

"""