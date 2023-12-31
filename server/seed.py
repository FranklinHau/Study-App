#!/usr/bin/env python3
import sys
sys.path.append("..")
# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from server.app import app
from app.models.user import db, User

if __name__ == '__main__':
    fake = Faker()

    # Initialize FLask app context
    with app.app_context():
        print("Starting seed...")
        
        # Delete existing data
        # This is to start with a clean stats 
        db.session.query(User).delete()

        # Number of users to create 
        num_users = 50

        # Create and add new users
        for _ in range(num_users):
            # Generate fake username and email 
            username = fake.user_name()
            email = fake.email()

            # Create new User instance
            # Using the fake username and email 
            new_user = User(username=username, email=email)

            # generate a fake password and set the hashed password for the user
            fake_password = fake.password()
            new_user.set_password(fake_password)

            # Add the new user to the database session
            # This prepares them to be committed to the database 
            db.session.add(new_user)

        # Commit the new users to the database 
        # Now, the database will actually be updated
        db.session.commit()

        print(f"Seeded {num_users} users!") 
