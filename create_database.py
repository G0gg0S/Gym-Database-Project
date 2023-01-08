import sqlite3
import os

if os.path.exists("Gym_database.db"):
  os.remove("Gym_database.db")
  print("Deleted the Gym database. Creating a new one...")
else:
  print("The Gym database does not exist. Creating a new one...")

conn = sqlite3.connect("Gym_database.db")

cursor = conn.cursor()

# Creation of "Administration" TABLE
cursor.execute("""
            DROP TABLE IF EXISTS "Administration";
            """)

cursor.execute("""
            CREATE TABLE IF NOT EXISTS Administration (
            level TEXT,
	          admin_ID INTEGER,
            PRIMARY KEY(admin_ID),
            FOREIGN KEY (admin_ID) REFERENCES Staff(staff_ID)
            );""")

print("Administration TABLE was created")

# Creation of "Class" TABLE
cursor.execute("""
            DROP TABLE IF EXISTS "Class";
            """)

cursor.execute("""
            CREATE TABLE IF NOT EXISTS Class (
            class_ID INTEGER,
            name TEXT,
            place TEXT,
            date TEXT,
            time TEXT,
            capacity INTEGER,
            gym_ID INTEGER,
            PRIMARY KEY(class_ID AUTOINCREMENT),
            FOREIGN KEY (gym_ID) REFERENCES Gym(gym_ID)
            );""")

print("Class TABLE was created")

# Creation of "Equipment" TABLE
cursor.execute("""
            DROP TABLE IF EXISTS "Equipment";
            """)

cursor.execute("""
            CREATE TABLE IF NOT EXISTS Equipment (
            equipment_ID INTEGER,
            purchase_date TEXT,
            working_period INTEGER,
            gym_ID INTEGER,
            PRIMARY KEY(equipment_ID AUTOINCREMENT),
            FOREIGN KEY (gym_ID) REFERENCES Gym(gym_ID)
            );""")

print("Equipment TABLE was created")

# Creation of "Gym" TABLE
cursor.execute("""
            DROP TABLE IF EXISTS "Gym";
            """)

cursor.execute("""
            CREATE TABLE IF NOT EXISTS Gym (
            address ΤΕΧΤ,
            town ΤΕΧΤ NOT NULL,
            capacity INTEGER,
            start_date TEXT,
            gym_ID INTEGER,
            phone TEXT,
            PRIMARY KEY(Gym_ID AUTOINCREMENT)
            );""")

print("Gym TABLE was created")

# Creation of "Instructor" TABLE
cursor.execute("""
            DROP TABLE IF EXISTS "Instructor";
            """)

cursor.execute("""
            CREATE TABLE IF NOT EXISTS Instructor (
            instructor_ID INTEGER,
            PRIMARY KEY(instructor_ID),
            FOREIGN KEY (instructor_ID) REFERENCES Staff(staff_ID)
            );""")

print("Instructor TABLE was created")

# Creation of "Maintenance" TABLE
cursor.execute("""
            DROP TABLE IF EXISTS "Maintenance";
            """)

cursor.execute("""
            CREATE TABLE IF NOT EXISTS Maintenance (
            service_company TEXT,
            maintenance_ID INTEGER,
            date TEXT,
            equipment_ID INTEGER,
            PRIMARY KEY(maintenance_ID, equipment_ID),
            FOREIGN KEY (equipment_ID) REFERENCES Equipment(equipment_ID)
            );""")

print("Maintenance TABLE was created")

# Creation of "Member" TABLE
cursor.execute("""
            DROP TABLE IF EXISTS "Member";
            """)

cursor.execute("""
            CREATE TABLE IF NOT EXISTS Member (
            name TEXT,
            surname TEXT,
            telephone INTEGER,
            email TEXT,
            start_date TEXT,
            age INTEGER,
            member_ID INTEGER,
            gym_ID INTEGER,
            gender TEXT,
            PRIMARY KEY(member_ID AUTOINCREMENT),
            FOREIGN KEY (gym_ID) REFERENCES Gym(gym_ID)
            );""")

print("Member TABLE was created")

# Creation of "Membership" TABLE
cursor.execute("""
            DROP TABLE IF EXISTS "Membership";
            """)

cursor.execute("""
            CREATE TABLE IF NOT EXISTS Membership (
            membership_ID INTEGER,
            type TEXT,
            rate INTEGER,
            start_date TEXT,
            expiration_date TEXT,
            gym_ID INTEGER,
            member_ID INTEGER,
            status TEXT,
            PRIMARY KEY(membership_ID, member_ID),
            FOREIGN KEY (gym_ID) REFERENCES Gym(gym_ID)
            );""")

print("Membership TABLE was created")

# Creation of "Payment" TABLE
cursor.execute("""
            DROP TABLE IF EXISTS "Payment";
            """)

cursor.execute("""
            CREATE TABLE IF NOT EXISTS Payment (
            amount INTEGER,
            date TEXT,
            membership_ID INTEGER,
            payment_ID INTEGER,               
            PRIMARY KEY(payment_ID, membership_ID),
            FOREIGN KEY (membership_ID) REFERENCES Membership(membership_ID) 
            );""")

print("Payment TABLE was created")

# Creation of "SignsUp" TABLE
cursor.execute("""
            DROP TABLE IF EXISTS "SignsUp";
            """)

cursor.execute("""
            CREATE TABLE IF NOT EXISTS SignsUp (
            member_ID INTEGER,
            class_ID INTEGER,
            PRIMARY KEY(member_ID,class_ID),
            FOREIGN KEY (member_ID) REFERENCES Member(member_ID),
            FOREIGN KEY (class_ID) REFERENCES Class(class_ID)
            );""")

print("SignsUp TABLE was created")

# Creation of "Staff" TABLE
cursor.execute("""
            DROP TABLE IF EXISTS "Staff";
            """)

cursor.execute("""
            CREATE TABLE IF NOT EXISTS Staff (
            staff_ID INTEGER,
            name TEXT,
            surname TEXT,
            salary INTEGER,
            start_date TEXT,
            birth_date TEXT,
            administration_ID INTEGER,
            gym_ID INTEGER,
            address TEXT,
            mobile_phone TEXT,
            PRIMARY KEY(staff_ID AUTOINCREMENT),
            FOREIGN KEY (gym_ID) REFERENCES Gym(gym_ID),
            FOREIGN KEY (administration_ID) REFERENCES Administration(admin_ID)
            );""")

print("Staff TABLE was created")

# Creation of "Teaches" TABLE
cursor.execute("""
            DROP TABLE IF EXISTS "Teaches";
            """)

cursor.execute("""
            CREATE TABLE IF NOT EXISTS Teaches (
            instructor_ID INTEGER,
            class_ID INTEGER,
            PRIMARY KEY(instructor_ID, class_ID),
            FOREIGN KEY (class_ID) REFERENCES Class(class_ID),
            FOREIGN KEY (instructor_ID) REFERENCES Instructor(instructor_ID)
            );""")

print("Teaches TABLE was created")



# Saving 
conn.commit();
conn.close();