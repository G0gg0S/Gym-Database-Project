import sqlite3, csv

connection = sqlite3.connect("Gym_database.db")
cursor = connection.cursor()

# Inserting data for the Administration Table
with open('data/Administration.csv', 'r') as file:
    no_records = 0
    for row in file:
        cursor.execute("INSERT INTO Administration VALUES (?, ?)", row.split(","))
        connection.commit()
        no_records += 1
print("Administration data inserted")

# Inserting data for the Class Table
with open('data/Class.csv', 'r') as file:
    no_records = 0
    for row in file:
        cursor.execute("INSERT INTO Class VALUES (?, ?, ?, ?, ?, ?, ?)", row.split(","))
        connection.commit()
        no_records += 1
print("Class data inserted")

# Inserting data for the Equipment Table
with open('data/Equipment.csv', 'r') as file:
    no_records = 0
    for row in file:
        cursor.execute("INSERT INTO Equipment VALUES (?, ?, ?, ?)", row.split(","))
        connection.commit()
        no_records += 1
print("Equipment data inserted")

# Inserting data for the Gym Table
with open('data/Gym.csv', 'r') as file:
    no_records = 0
    for row in file:
        cursor.execute("INSERT INTO Gym VALUES (?, ?, ?, ?, ?, ?)", row.split(","))
        connection.commit()
        no_records += 1
print("Gym data inserted")

# Inserting data for the Instructor Table
with open('data/Instructor.csv', 'r') as file:
    no_records = 0
    for row in file:
        cursor.execute("INSERT INTO Instructor VALUES (?)", row.split(","))
        connection.commit()
        no_records += 1
print("Instructor data inserted")

# Inserting data for the Maintenance Table
with open('data/Maintenance.csv', 'r') as file:
    no_records = 0
    for row in file:
        cursor.execute("INSERT INTO Maintenance VALUES (?, ?, ?, ?)", row.split(","))
        connection.commit()
        no_records += 1
print("Maintenance data inserted")

# Inserting data for the Member Table
with open('data/Member.csv', 'r') as file:
    no_records = 0
    for row in file:
        cursor.execute("INSERT INTO Member VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", row.split(","))
        connection.commit()
        no_records += 1
print("Member data inserted")

# Inserting data for the Membership Table
with open('data/Membership.csv', 'r') as file:
    no_records = 0
    for row in file:
        cursor.execute("INSERT INTO Membership VALUES (?, ?, ?, ?, ?, ?, ?, ?)", row.split(","))
        connection.commit()
        no_records += 1
print("Membership data inserted")

# Inserting data for the Payment Table
with open('data/Payment.csv', 'r') as file:
    no_records = 0
    for row in file:
        cursor.execute("INSERT INTO Payment VALUES (?, ?, ?, ?)", row.split(","))
        connection.commit()
        no_records += 1
print("Payment data inserted")

# Inserting data for the SignsUp Table
with open('data/SignsUp.csv', 'r') as file:
    no_records = 0
    for row in file:
        cursor.execute("INSERT INTO SignsUp VALUES (?, ?)", row.split(","))
        connection.commit()
        no_records += 1
print("SignsUp data inserted")

# Inserting data for the Staff Table
with open('data/Staff.csv', 'r') as file:
    no_records = 0
    for row in file:
        cursor.execute("INSERT INTO Staff VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", row.split(","))
        connection.commit()
        no_records += 1
print("Staff data inserted")

# Inserting data for the Teaches Table
with open('data/Teaches.csv', 'r') as file:
    no_records = 0
    for row in file:
        cursor.execute("INSERT INTO Teaches VALUES (?, ?)", row.split(","))
        connection.commit()
        no_records += 1
print("Teaches data inserted")

connection.close()
