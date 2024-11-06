import sqlite3

# Connect to the database
conn = sqlite3.connect('example.db')
c = conn.cursor()

# Create tables
c.execute('''CREATE TABLE Users (id INTEGER PRIMARY KEY, name TEXT, email TEXT UNIQUE, date_of_birth TEXT)''')
c.execute('''CREATE TABLE Profiles (user_id INTEGER PRIMARY KEY, bio TEXT, profile_picture TEXT, joined_date TEXT, FOREIGN KEY(user_id) REFERENCES Users(id))''')

# Insert data
c.execute("INSERT INTO Users (name, email, date_of_birth) VALUES ('Alice', 'Alice@gmail.com', '21/10/1999')")
c.execute("INSERT INTO Profiles (user_id, bio, profile_picture, joined_date) VALUES (1, 'Hello, I am Alice.','picture','06/11/2024')")

c.execute("INSERT INTO Users (name, email, date_of_birth) VALUES ('Bob', 'bob@gmail.com', '15/05/1995')")
c.execute("INSERT INTO Profiles (user_id, bio, profile_picture, joined_date) VALUES (2, 'Hey there, I am Bob.', 'picture2', '06/11/2024')")

c.execute("INSERT INTO Users (name, email, date_of_birth) VALUES ('Charlie', 'charlie123@gmail.com', '12/12/1988')")
c.execute("INSERT INTO Profiles (user_id, bio, profile_picture, joined_date) VALUES (3, 'Welcome to my profile. I am Charlie.', 'charlie_pic', '06/11/2024')")

c.execute("INSERT INTO Users (name, email, date_of_birth) VALUES ('Eve', 'eve.heart@gmail.com' , '09/09/1992')")
c.execute("INSERT INTO Profiles (user_id, bio, profile_picture, joined_date) VALUES (5, 'Eves profile!', 'eve_picture', '06/11/2024')")


conn.commit()
conn.close()
