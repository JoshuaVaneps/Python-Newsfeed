from app.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates
import bcrypt

salt = bcrypt.gensalt()

class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True)
  username = Column(String(50), nullable=False)
  email = Column(String(50), nullable=False, unique=True)
  password = Column(String(100), nullable=False)


# validate_email() method returns what the value of the email column should be, and the @validates() decorator internally handles the rest.
  @validates('email')
  def validate_email(self, key, email):
    # make sure email address contains @ character
    assert '@' in email

    return email

# The validate_password() function returns an encrypted version of the password, if the assert doesn't throw an error.
  @validates('password')
  def validate_password(self, key, password):
    assert len(password) > 4
    # encrypt password
    return bcrypt.hashpw(password.encode('utf-8'), salt)

