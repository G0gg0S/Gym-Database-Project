import sqlite3, os,sys,traceback

# Checks if the db exists and connects. If not, terminates the app
if os.path.exists("Gym_database.db"):
  print("Connecting to Gym Database...")
  connection = sqlite3.connect("Gym_database.db")
  cursor = connection.cursor()
  print("Hello There! Welcome to the Gym database!")
else:
  print("The Gym database does not exist!")

# This function handles the data insertion process
def insert():
    print("Choose 1 of the following options:")
    print("'1' for Membership insertion")
    print("'2' for Payment insertion")
    print("'3' for Member insertion")
    print("'4' for Equipment insertion")
    print("'5' for Staff insertion")
    print("'6' for Gym insertion")
    print("'7' for Maintenance insertion")
    print("'8' for SignsUp insertion")
    print("'9' for Teaches insertion")
    print("'10' for Class insertion")
    action = input()
    print_dashes()
    match action:
        case "1":
            #90,silver,50,17/02/2022,17/03/2022,5,30,active
            print("You chose new Membership insertion")
            print("Provide the following separated with commas:")
            print("- Membership ID")
            print("- Type")
            print("- Rate")
            print("- Start Date")
            print("- Expiration Date")
            print("- Gym ID")
            print("- Member ID")
            print("- Status")
            user_input = input()
            try:
                cursor.execute("INSERT INTO Membership VALUES (?, ?, ?, ?, ?, ?, ?, ?)", user_input.split(",")) 
                connection.commit()
                print("Your command successfully executed!")   
            except sqlite3.Error as er:
                print("Your command DID NOT executed because of input Error! Check your inputs and try again. The following error was generated.")
                print(er)        
        case "2":
            #20,17/06/2022,46,54
            print("You chose new Payment insertion")
            print("Provide the following separated with commas:")
            print("- Amount")
            print("- Date")            
            print("- Membership ID")
            print("- Payment ID")
            user_input = input()
            try:
                cursor.execute("INSERT INTO Payment VALUES (?, ?, ?, ?)", user_input.split(",")) 
                connection.commit()
                print("Your command successfully executed!")
            except sqlite3.Error as er:
                print("Your command DID NOT executed because of input Error! Check your inputs and try again. The following error was generated.")
                print(er)
        case "3":
            #Dimitra,Anagn,698,email,17/02/2022,23,9,Male
            print("You chose new Member insertion")
            print("Provide the following separated with commas:")
            print("- Name")
            print("- Surname")
            print("- Telephone")
            print("- Email")
            print("- Start date")
            print("- Age")
            print("- Gym ID")
            print("- Gender")
            user_input = input()
            try:    
                cursor.execute("INSERT INTO Member (name,surname,telephone,email,start_date,age,gym_ID,gender) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", user_input.split(",")) 
                connection.commit()
                print("Your command successfully executed!")
            except sqlite3.Error as er:
                print("Your command DID NOT executed because of input Error! Check your inputs and try again. The following error was generated.")
                print(er)
        case "4":
            #17/06/2022,1,10
            print("You chose new Equipment insertion")
            print("Provide the following separated with commas:")
            print("- Purchase date")            
            print("- Working period")
            print("- Gym ID")
            user_input = input()
            try:
                cursor.execute("INSERT INTO Equipment (purchase_date,working_period,gym_ID) VALUES (?, ?, ?)", user_input.split(",")) 
                connection.commit()
                print("Your command successfully executed!")
            except sqlite3.Error as er:
                print("Your command DID NOT executed because of input Error! Check your inputs and try again. The following error was generated.")
                print(er)
        case "5":
            #Dimitra,Anagn,5985,17/02/2022,17/02/1999,23,9,Al,698 no level included
            print("You chose new Staff insertion")
            print("Choose 1 of the following options:")
            print("'1' for Instructor insertion")
            print("'2' for Administration insertion")
            user_staff = input()
            print("Provide the following separated with commas:")
            print("- Name")
            print("- Surname")
            print("- Salary")
            print("- Start date")
            print("- Birth date")
            print("- Administration ID")
            print("- Gym ID")
            print("- Address")
            print("- Mobile phone")
            match user_staff:
                case "2":
                    print("- Level")
            user_input = input()
            a = user_input.split(",")
            try:
                match user_staff:
                    case "1":
                        cursor.execute("INSERT INTO Staff (name,surname,salary,start_date,birth_date,administration_ID,gym_ID,address,mobile_phone) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", a)
                    case "2":
                        cursor.execute("INSERT INTO Staff (name,surname,salary,start_date,birth_date,administration_ID,gym_ID,address,mobile_phone) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", a[:-1]) 
                
                cursor.execute("SELECT staff_ID FROM Staff ORDER BY staff_ID DESC LIMIT 1;")
                data = cursor.fetchall()
                match user_staff:
                    case "1":
                        cursor.execute("INSERT INTO Instructor VALUES ({0})".format(data[0][0]))
                    case "2":
                        cursor.execute("INSERT INTO Administration VALUES ({0},{1})".format(a[-1],data[0][0]))
                connection.commit()
                print("Your command successfully executed!")
            except sqlite3.Error as er:
                print("Your command DID NOT executed because of input Error! Check your inputs and try again. The following error was generated.")
                print(er)
            
        case "6":
            #Al.IP54,Patras,200,17/02/2022,698
            print("You chose new Gym insertion")
            print("Provide the following separated with commas:")
            print("- Address")
            print("- Town")
            print("- Capacity")
            print("- Start date")
            print("- Phone")
            user_input = input()
            try:
                cursor.execute("INSERT INTO Gym (address,town,capacity,start_date,phone) VALUES (?, ?, ?, ?, ?)", user_input.split(",")) 
                connection.commit()
                print("Your command successfully executed!")
            except sqlite3.Error as er:
                print("Your command DID NOT executed because of input Error! Check your inputs and try again. The following error was generated.")
                print(er)
        case "7":
            #PSOLAS AE,50,17/02/2022,30
            print("You chose new Maintenance insertion")
            print("Provide the following separated with commas:")
            print("- Service company")
            print("- Maintenance ID")
            print("- Date")
            print("- Equipment ID")
            user_input = input()
            try:
                cursor.execute("INSERT INTO Maintenance VALUES (?, ?, ?, ?)", user_input.split(",")) 
                connection.commit()
                print("Your command successfully executed!")
            except sqlite3.Error as er:
                print("Your command DID NOT executed because of input Error! Check your inputs and try again. The following error was generated.")
                print(er)
        case "8":
            #50,30
            print("You chose new Sign Up insertion")
            print("Provide the following separated with commas:")
            print("- Member ID")
            print("- Class ID")
            user_input = input()
            try:
                cursor.execute("INSERT INTO SignsUp VALUES (?, ?)", user_input.split(",")) 
                connection.commit()
                print("Your command successfully executed!")
            except sqlite3.Error as er:
                print("Your command DID NOT executed because of input Error! Check your inputs and try again. The following error was generated.")
                print(er)
        case "9":
            #50,30
            print("You chose new Instructor Class Assignment insertion")
            print("Provide the following separated with commas:")
            print("- Instructor ID")
            print("- Class ID")
            user_input = input()
            try:
                cursor.execute("INSERT INTO Teaches VALUES (?, ?)", user_input.split(",")) 
                connection.commit()
                print("Your command successfully executed!")
            except sqlite3.Error as er:
                print("Your command DID NOT executed because of input Error! Check your inputs and try again. The following error was generated.")
                print(er)
        case "10":
            #Pilates,Room5,17/02/2022,23:05,15,10
            print("You chose new Class insertion")
            print("Provide the following separated with commas:")
            print("- Name")
            print("- Place")
            print("- Date")
            print("- Time")
            print("- Capacity")
            print("- Gym ID")
            user_input = input()
            try:
                cursor.execute("INSERT INTO Class (name,place,date,time,capacity,gym_ID) VALUES (?, ?, ?, ?, ?, ?)", user_input.split(",")) 
                connection.commit()
                print("Your command successfully executed!")      
            except sqlite3.Error as er:
                print("Your command DID NOT executed because of input Error! Check your inputs and try again. The following error was generated.")
                print(er)     
        case other:
            print("other")
    continue_message()    

# This function handles the data delete process
def delete():
    print("Delete func was called")
    print("Choose 1 of the following options:")
    print("'1' for Instructor Class Assignment deletion")
    print("'2' for Member Class Sign Up deletion")
    print("'3' for Instructor Staff deletion")
    print("'4' for Administration Staff deletion")
    print("'5' for Class deletion")
    print("'6' for Equipment deletion")
    action = input()
    match action:
        case "1":
            print("1")
            print("You chose Instructor Class Assignment deletion")
            print("Provide the following separated with commas:")
            print("- Instructor ID")
            print("- Class ID")
            user_input = input()
            try:
                cursor.execute("DELETE FROM Teaches WHERE instructor_ID = ? AND class_ID = ?", user_input.split(",")) 
                connection.commit()
                print("Your command successfully executed!")
            except sqlite3.Error as er:
                print("Your command DID NOT executed because of input Error! Check your inputs and try again. The following error was generated.")
                print(er)
        case "2":
            print("2")
            print("You chose Member Class Sign Up deletion")
            print("Provide the following separated with commas:")
            print("- Member ID")
            print("- Class ID")
            user_input = input()
            try:
                cursor.execute("DELETE FROM SignsUp WHERE member_ID = ? AND class_ID = ?", user_input.split(",")) 
                connection.commit()
                print("Your command successfully executed!")
            except sqlite3.Error as er:
                print("Your command DID NOT executed because of input Error! Check your inputs and try again. The following error was generated.")
                print(er)
        case "3":
            print("3")
            print("You chose Instructor deletion")
            print("Provide the following separated with commas:")
            print("- Instructor ID")
            user_input = input()
            try:
                cursor.execute("DELETE FROM Staff WHERE staff_ID = {0} ".format(user_input))
                cursor.execute("DELETE FROM Instructor WHERE instructor_ID = {0} ".format(user_input))
                cursor.execute("DELETE FROM Teaches WHERE instructor_ID = {0} ".format(user_input))
                connection.commit()
                print("Your command successfully executed!")
            except sqlite3.Error as er:
                print("Your command DID NOT executed because of input Error! Check your inputs and try again. The following error was generated.")
                print(er)
        case "4":
            print("4")
            print("You chose Administration deletion")
            print("Provide the following separated with commas:")
            print("- Administration ID")
            user_input = input()
            try:
                cursor.execute("DELETE FROM Staff WHERE staff_ID = {0} ".format(user_input))
                cursor.execute("DELETE FROM Administration WHERE admin_ID = {0} ".format(user_input))
                connection.commit()
                print("Your command successfully executed!")
            except sqlite3.Error as er:
                print("Your command DID NOT executed because of input Error! Check your inputs and try again. The following error was generated.")
                print(er)
        case "5":
            print("5")
            print("You chose Class deletion")
            print("Provide the following separated with commas:")
            print("- Class ID")
            user_input = input()
            try:
                cursor.execute("DELETE FROM Class WHERE class_ID = {0} ".format(user_input))
                cursor.execute("DELETE FROM Teaches WHERE class_ID = {0} ".format(user_input))
                cursor.execute("DELETE FROM SignsUp WHERE class_ID = {0} ".format(user_input))
                connection.commit()
                print("Your command successfully executed!")
            except sqlite3.Error as er:
                print("Your command DID NOT executed because of input Error! Check your inputs and try again. The following error was generated.")
                print(er)
        case "6":
            print("6")
            print("You chose Equipment deletion")
            print("Provide the following separated with commas:")
            print("- Equipment ID")
            user_input = input()
            try:
                cursor.execute("DELETE FROM Equipment WHERE equipment_ID = {0} ".format(user_input))
                cursor.execute("DELETE FROM Maintenance WHERE equipment_ID = {0} ".format(user_input))
                connection.commit()
                print("Your command successfully executed!")
            except sqlite3.Error as er:
                print("Your command DID NOT executed because of input Error! Check your inputs and try again. The following error was generated.")
                print(er)
        case other:
            pass
    continue_message()

# This function handles the data update process
def update():
    print("Update func was called")
    print("Choose 1 of the following options:")
    print("'1' for Membership update")
    print("'2' for Payment update")
    print("'3' for Member update")
    print("'4' for Equipment update")
    print("'5' for Staff update")
    print("'6' for Gym update")
    print("'7' for Maintenance update")
    print("'8' for SignsUp update")
    print("'9' for Teaches update")
    print("'10' for Class update")
    print("'11' for Administration Level update")
    action = input()
    print_dashes()

    match action:
        case "1":
            table = "Membership"
            relationIds = ["membership_ID", "member_ID"]
            print("Provide me with the Membership ID and Member ID")
            pass
        case "2":
            relationIds = ["payment_ID", "membership_ID"]
            table = "Payment"
            print("Provide me with the Payment ID and Membership ID")
            pass
        case "3":
            relationIds = ["member_ID"]
            table = "Member"
            print("Provide me with the Member ID")
            pass
        case "4":
            relationIds = ["equipment_ID"]
            table = "Equipment"
            print("Provide me with the Equipment ID number")
            pass
        case "5":
            relationIds = ["staff_ID"]
            table = "Staff"
            print("Provide me with the Staff ID")
            pass
        case "6":
            relationIds = ["gym_ID"]
            table = "Gym"
            print("Provide me with the Gym ID")
            pass
        case "7":
            relationIds = ["maintenance_ID", "equipment_ID"]
            table = "Maintenance"
            print("Provide me with the Maintenance ID and Equipment ID")
            pass
        case "8":
            relationIds = ["member_ID", "class_ID"]
            table = "SignsUp"
            print("Provide me with the Member ID and Class ID")
            pass
        case "9":
            relationIds = ["instructor_ID", "class_ID"]
            table = "Teaches"
            print("Provide me with the Instructor ID and Class ID")
            pass
        case "10":
            relationIds = ["class_ID"]
            table = "Class"
            print("Provide me with the Class ID")
        case "11":
            relationIds = ["admin_ID"]
            table = "Administration"
            print("Provide me with the Administration ID")
    ids = input()
    ids = ids.split(",")
    print_dashes()
    if(len(relationIds)!=len(ids)):
        print("Your command DID NOT executed because of input Error! Check your inputs and try again.")
        continue_message()
        return

    print("Insert which attributes to update, separated with commas")
    match action:
        case "1":
            # 90,silver,50,17/02/2022,17/03/2022,5,30,active
            relationAtrr = ["membership_ID","type","rate","start_date","expiration_date", "gym_ID", "member_ID", "status"]
            print("'1' for Membership ID")
            print("'2' for Type")
            print("'3' for Rate")
            print("'4' for Start Date")
            print("'5' for Expiration Date")
            print("'6' for Gym ID")
            print("'7' for Member ID")
            print("'8' for Status")
            pass
        case "2":
            relationAtrr = ["amount","date","membership_ID","payment_ID"]
            print("'1' for Amount")
            print("'2' for Date")            
            print("'3' for Membership ID")
            print("'4' for Payment ID")
            pass
        case "3":
            relationAtrr = ["name","surname","telephone","email", "start_date", "age", "gym_ID","gender"]
            print("'1' for Name")
            print("'2' for Surname")
            print("'3' for Telephone")
            print("'4' for Email")
            print("'5' for Start date")
            print("'6' for Age")
            print("'7' for Gym ID")
            print("'8' for Gender")
            pass
        case "4":
            relationAtrr = ["purchase_date","working_period","gym_ID"]
            print("'1' for Purchase date")            
            print("'2' for Working period")
            print("'3' for Gym ID")
            pass
        case "5":
            relationAtrr = ["name","surname","salary","start_date", "birth_date", "administration_ID","gym_ID","address","mobile_phone"]
            print("'1' for Name")
            print("'2' for Surname")
            print("'3' for Salary")
            print("'4' for Start date")
            print("'5' for Birth date")
            print("'6' for Administration ID")
            print("'7' for Gym ID")
            print("'8' for Address")
            print("'9' for Mobile phone")
            pass
        case "6":
            relationAtrr = ["address","town","capacity","start_date","phone"]
            print("'1' for Address")
            print("'2' for Town")
            print("'3' for Capacity")
            print("'4' for Start date")
            print("'5' for Phone")
            pass
        case "7":
            relationAtrr = ["service_company","maintenance_ID","date","equipment_ID"]
            print("'1' for Service company")
            print("'2' for Maintenance ID")
            print("'3' for Date")
            print("'4' for Equipment ID")
            pass
        case "8":
            relationAtrr = ["member_ID","class_ID"]
            print("'1' for Member ID")
            print("'2' for Class ID")
            pass
        case "9":
            relationAtrr = ["instructor_ID","class_ID"]
            print("'1' for Instructor ID")
            print("'2' for Class ID")
            pass
        case "10":
            relationAtrr = ["name","place","date","time", "capacity","gym_ID"]
            print("'1' for Name")
            print("'2' for Place")
            print("'3' for Date")
            print("'4' for Time")
            print("'5' for Capacity")
            print("'6' for Gym ID")
            pass
        case "11":
            relationAtrr = ["level"]
            print("'1' for Level")

    data_to_change = input();
    print_dashes()
    data_to_change = data_to_change.split(",")
    print("Insert the updated data separated with commas")
    new_data = input();
    print_dashes()
    new_data = new_data.split(",")    

    try:
        if(len(new_data)!=len(data_to_change)):
            print("Your command DID NOT executed because of input Error! Check your inputs and try again.")
        elif(len(ids) == 1):
            i=0
            for a in data_to_change:
                index = int(a)-1
                print("""UPDATE {0} SET {1} = "{2}" WHERE {3} = {4}""".format(table,relationAtrr[index],new_data[i],relationIds[0],ids[0]))
                cursor.execute("""UPDATE {0} 
                                    SET {1} = "{2}" 
                                    WHERE {3} = {4}""".format(table,relationAtrr[index],new_data[i],relationIds[0],ids[0]))
                connection.commit()
                i+=1
            print("Your command successfully executed!")
        elif(len(ids) == 2):
            i=0
            for a in data_to_change:
                index = int(a)-1
                print("""UPDATE {0} SET {1} = "{2}" WHERE {3} = {4} AND {5} = {6}""".format(table,relationAtrr[index],new_data[i],relationIds[0],ids[0],relationIds[1],ids[1]))
                cursor.execute("""UPDATE {0} 
                                    SET {1} = "{2}" 
                                    WHERE {3} = {4} AND {5} = {6}""".format(table,relationAtrr[index],new_data[i],relationIds[0],ids[0],relationIds[1],ids[1]))
                connection.commit()
                i+=1
            print("Your command successfully executed!")
        
    except sqlite3.Error as er:
                print("Your command DID NOT executed because of input Error! Check your inputs and try again. The following error was generated.")
                print(er)
    except IndexError as er:
                print("Your command DID NOT executed because of input Error! Check your inputs and try again. The following error was generated.")
                print(er)
    continue_message()

# This function handles the raw query insertion process
def query():
    print("Query func was called")
    print("Provide the SQLite query.")
    query = input()
    print_dashes()
    print("The query you inserted: {0}".format(query))    
    try:
        cursor.execute(query)
        data = cursor.fetchall()
        style="{:<25}"
        names = list(map(lambda x: x[0], cursor.description))
        for element in names:
            print(style.format(element),end="")
        print("\n")
        for	row	in	data:
            for element in row:	
                print(style.format(element),end="")
            print()
            
    except sqlite3.Error as er:
        print("Your command DID NOT executed because of input Error! Check your inputs and try again. The following error was generated.")
        print(er)
    
    continue_message()

def continue_message():
    print("Press any key to continue...")
    input()
    print_dashes()
    

def print_dashes():
    print("--------------------------------------------------------------------------")


while(os.path.exists("Gym_database.db")):
    print("The Following actions can be performed.")
    print("- Press I for INSERT")
    print("- Press D for DELETE")
    print("- Press U for UPDATE")
    print("- Press C for Query")
    print("- Press Q for Termination")
    action = input()
    print_dashes()
    if(action!="I" and action!="D" and action!="U" and action!="C" and action!="Q"):
        print("Ups. Press ENTER for another try")
        continue

    if(action == "Q"):
        print("Q pressed")
        break    

    match action:
        case "I":
            insert()
            continue
        case "D":
            delete()
            continue
        case "U":
            update()
            continue
        case "C":
            query()
            continue


print("Closing connection to database..Bye")
connection.close()


