import mysql.connector

mycon=None
mycursor=None
flag=0
sp=""


def check_connection():

    mycon = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="password"
    )
    
    if mycon.is_connected():
        print("Successfully connected to MySQL")
        flag=1
        
    return flag



def create_database():
    
    mycon = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="password"
    )

    mycursor = mycon.cursor()

    mycursor.execute("CREATE DATABASE IF NOT EXISTS billing_database")
   
    print("Database created and used")




def create_table():
    
    mycon = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="password",
      database="billing_database"
    )

    mycursor = mycon.cursor()

    mycursor.execute("CREATE TABLE IF NOT EXISTS billing_system(customerid int(5),customername varchar(20),contact int(11),address varchar(20),billnumber int(20),gasconsumed int(10),totalamount int(10))")

    print("Tables under billing_databse: ")

    mycursor.execute("SHOW TABLES")

    for x in mycursor:
        print(x)




def add_new_record():
    
    mycon = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="password",
      database="billing_database"
    )
    mycursor = mycon.cursor()
    

    customerid=int(input("Enter Customer's id:\n"))
    
    customername=input("Enter Customer's Name:\n")
    
    contact=int(input("Enter Customer's Phone Number:\n"))
    
    address=input("Enter Customer's Address:\n")
    
    billnumber=int(input("Enter Bill Number:\n"))
    
    gasconsumed=int(input("Enter Gas consumed:\n"))
    print("")

    sql = "INSERT INTO billing_system(customerid,customername,contact,address,billnumber,gasconsumed) VALUES({},'{}',{},'{}',{},{})".format(customerid,customername,contact,address,billnumber,gasconsumed)
   
    mycursor.execute(sql)
   
    mycon.commit()

    c = mycursor.rowcount
    
    if (c>1):
        print(c, "records inserted")
        
    else:
        print("1 record inserted")




def space(V):
    
    global sp
    sp = ""
    l = 15-len(str(V))
    for i in range(l):
        sp = sp+" "
    return sp




def display_all_record():
   
    mycon = mysql.connector.connect(
      host = "localhost",
      user = "root",
      passwd = "password",
      database = "billing_database"
    )


    mycursor = mycon.cursor()

    mycursor.execute("SELECT * FROM billing_system")

    myresult = mycursor.fetchall()

    print("---------------------------------------------------------------------------------------------------------------------")
    print("CUSTOMER ID",space("CUSTOMER ID"),"CUSTOMER NAME", space("CUSTOMER NAME"),"CONTACT NUMBER",space("CONTACT NUMBER"),"ADDRESS",space("ADDRESS"),"BILL NUMBER",space("BILL NUMBER"),"GAS CONSUMED(lit)",space("GAS CONSUMED(lit)"),"TOTAL AMOUNT")          
    print("---------------------------------------------------------------------------------------------------------------------")

    for x in myresult:
        print(x[0],space(str(x[0])),x[1],space(x[1]),x[2],space(x[2]),x[3],space(x[3]),x[4],space(x[4]),x[5],space(x[5]),"  ",78*int(x[5]))

    print("---------------------------------------------------------------------------------------------------------------------")




def search_record():
   
    mycon = mysql.connector.connect(
      host = "localhost",
      user = "root",
      passwd = "password",
      database = "billing_database"
    )


    mycursor = mycon.cursor()

    CUSTOMER_ID = int(input("Enter customer's id to search\n"))
   
    print("")
   
    sql_select_query = "select * from billing_system where customerid = %s"

    mycursor.execute(sql_select_query, (CUSTOMER_ID, ))

    myresult = mycursor.fetchall()
   
    c = mycursor.rowcount
   
    if (c>0):
       
        print("---------------------------------------------------------------------------------------------------------------------")
        print("CUSTOMER ID",space("CUSTOMER ID"),"CUSTOMER NAME", space("CUSTOMER NAME"),"CONTACT NUMBER",space("CONTACT NUMBER"),"ADDRESS",space("ADDRESS"),"BILL NUMBER",space("BILL NUMBER"),"GAS CONSUMED(lit)",space("GAS CONSUMED(lit)"),"TOTAL AMOUNT")
        print("---------------------------------------------------------------------------------------------------------------------")

        for x in myresult:
            print(x[0],space(str(x[0])),x[1],space(x[1]),x[2],space(x[2]),x[3],space(x[3]),x[4],space(x[4]),x[5],space(x[5]),"  ",78*int(x[5]))
         
        print("---------------------------------------------------------------------------------------------------------------------")
   
    else:

        print("No data to display")




def delete_record():

    mycon = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="password",
      database="billing_database"
    )


    mycursor = mycon.cursor()
   
    CUSTOMER_ID = int(input("Enter customer id to delete\n"))
    print("")

    sql_select_query = "DELETE FROM billing_system WHERE customerid = %s"

    mycursor.execute(sql_select_query, (CUSTOMER_ID, ))

    mycon.commit()

    c = mycursor.rowcount
    
    if (c > 1):
        print(c, "records deleted")
   
    elif ( c==1 ):
        print("1 record deleted")
   
    else:
        print("No such record exists")
   
    mycursor.execute("SELECT * FROM billing_system")

    myresult = mycursor.fetchall()
    print("")
   
    print("---------------------------------------------------------------------------------------------------------------------")
    print("CUSTOMER ID",space("CUSTOMER ID"),"CUSTOMER NAME", space("CUSTOMER NAME"),"CONTACT NUMBER",space("CONTACT NUMBER"),"ADDRESS",space("ADDRESS"),"BILL NUMBER",space("BILL NUMBER"),"GAS CONSUMED(lit)",space("GAS CONSUMED(lit)"),"TOTAL AMOUNT")
    print("---------------------------------------------------------------------------------------------------------------------")

    for x in myresult:
        print(x[0],space(str(x[0])),x[1],space(x[1]),x[2],space(x[2]),x[3],space(x[3]),x[4],space(x[4]),x[5],space(x[5]),"  ",78*int(x[5]))
        
    print("---------------------------------------------------------------------------------------------------------------------")




def update_record():
    
    mycon = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="password",
      database="billing_database"
    )

    mycursor = mycon.cursor()
   
    CUSTOMER_ID = int(input("Enter customer id to update\n"))
    print("")
    
   
    New_GAS_CONSUMED = int(input("Enter new gas consumed by the customer\n"))
    print("")

    sql_select_query = "UPDATE billing_system set gasconsumed = %s WHERE customerid = %s"
   
    r = (New_GAS_CONSUMED, CUSTOMER_ID)

    mycursor.execute(sql_select_query, r)

    mycon.commit()
   
    c = mycursor.rowcount
    
    if (c > 1):
        print(c,"\nrecords updated")
   
    elif (c == 1):
        print("\n1 record updated")
       
    else:
        print("\nNo such record exists")
        
    print("")
    print("")

    mycursor.execute("SELECT * FROM billing_system")

    myresult = mycursor.fetchall()
   
    print("---------------------------------------------------------------------------------------------------------------------")
    print("CUSTOMER ID",space("CUSTOMER ID"),"CUSTOMER NAME", space("CUSTOMER NAME"),"CONTACT NUMBER",space("CONTACT NUMBER"),"ADDRESS",space("ADDRESS"),"BILL NUMBER",space("BILL NUMBER"),"GAS CONSUMED(lit)",space("GAS CONSUMED(lit)"),"TOTAL AMOUNT",space("TOTAL AMOUNT"))
    print("---------------------------------------------------------------------------------------------------------------------")

    for x in myresult:
        print(x[0],space(str(x[0])),x[1],space(x[1]),x[2],space(x[2]),x[3],space(x[3]),x[4],space(x[4]),x[5],space(x[5]),"  ",78*int(x[5]))
        
    print("---------------------------------------------------------------------------------------------------------------------")




def display_user():
    mycon = mysql.connector.connect(
      host = "localhost",
      user = "root",
      passwd = "password",
      database = "billing_database"
    )


    mycursor = mycon.cursor()

    passwd = int(input("Enter your password\n"))
    print("")

    sql_select_query = "select * from billing_system where contact = %s"

    mycursor.execute(sql_select_query, (passwd, ))

    myresult = mycursor.fetchall()

    c = mycursor.rowcount
   
    if (c>0):
       
        print("---------------------------------------------------------------------------------------------------------------------")
        print("CUSTOMER ID",space("CUSTOMER ID"),"CUSTOMER NAME", space("CUSTOMER NAME"),"CONTACT NUMBER",space("CONTACT NUMBER"),"ADDRESS",space("ADDRESS"),"BILL NUMBER",space("BILL NUMBER"),"GAS CONSUMED(lit)",space("GAS CONSUMED(lit)"),"TOTAL AMOUNT")
        print("---------------------------------------------------------------------------------------------------------------------")

        for x in myresult:
            print(x[0],space(str(x[0])),x[1],space(x[1]),x[2],space(x[2]),x[3],space(x[3]),x[4],space(x[4]),x[5],space(x[5]),"  ",78*int(x[5]))
         
        print("---------------------------------------------------------------------------------------------------------------------")
   
    else:

        print("No user exists with this password")




def update_user():
    mycon = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="password",
      database="billing_database"
    )

    mycursor = mycon.cursor()

    passwd = int(input("Enter your password\n"))
   
    New_GAS_CONSUMED = int(input("Enter new gas consumed by the customer\n"))
    print("")

    sql_select_query = "UPDATE billing_system set gasconsumed = %s WHERE contact = %s"
   
    r = (New_GAS_CONSUMED, passwd)

    mycursor.execute(sql_select_query, r)

    mycon.commit()
   
    c = mycursor.rowcount
    
    if (c > 1):
        print(c,"records updated")
   
    elif (c == 1):
        print("1 record updated")
       
    else:
        print("No user exists with this password")
        
    print("")
    

    sqlselect_query = "select * from billing_system where contact = %s"

    mycursor.execute(sqlselect_query, (passwd, ))

    my_result = mycursor.fetchall()

    counter = mycursor.rowcount
   
    if (counter>0):
       
        print("---------------------------------------------------------------------------------------------------------------------")
        print("CUSTOMER ID",space("CUSTOMER ID"),"CUSTOMER NAME", space("CUSTOMER NAME"),"CONTACT NUMBER",space("CONTACT NUMBER"),"ADDRESS",space("ADDRESS"),"BILL NUMBER",space("BILL NUMBER"),"GAS CONSUMED(lit)",space("GAS CONSUMED(lit)"),"TOTAL AMOUNT")
        print("---------------------------------------------------------------------------------------------------------------------")

        for x in my_result:
            print(x[0],space(str(x[0])),x[1],space(x[1]),x[2],space(x[2]),x[3],space(x[3]),x[4],space(x[4]),x[5],space(x[5]),"  ",78*int(x[5]))
         
        print("---------------------------------------------------------------------------------------------------------------------")




def admin():

    ans = 'yes'

    while (ans == 'yes' or ans == 'Yes'):

        print("")
        print("")
    
        print("\t\t\t**********************************************************************")
        print("\t\t\t*\t\t\tGAS BILLING SYSTEM                           *")
        print("\t\t\t*\t\t\t                                             *")
        print("\t\t\t*\t\t\t  1>  Add                                    *")
        print("\t\t\t*\t\t\t  2>  Display                                *")
        print("\t\t\t*\t\t\t  3>  Search                                 *")
        print("\t\t\t*\t\t\t  4>  Delete                                 *")
        print("\t\t\t*\t\t\t  5>  Update                                 *")
        print("\t\t\t*\t\t\t  6>  Return                                 *")
        print("\t\t\t**********************************************************************\n")
 
    
        print("")
        ch = int(input("Enter your choice\n"))
        print("")

        
        if (ch == 1):
            add_new_record()
            
        elif (ch == 2):
            display_all_record()
        
        elif (ch == 3):
            search_record()
        
        elif (ch == 4):
            delete_record()
        
        elif (ch == 5):
            update_record()
        
        elif (ch == 6):
            break
        
        else:
            print("Wrong Choice, Please enter values between 1-6")




def user():

    b = 'yes'

    while(b == 'yes'):
        print("")
        print("")

        print("\t\t\t**********************************************************************")
        print("\t\t\t*\t\t\tGas Billing System                           *")
        print("\t\t\t*\t\t\t                                             *")
        print("\t\t\t*\t\t\t  1>  Display                                *")
        print("\t\t\t*\t\t\t  2>  Update                                 *")
        print("\t\t\t*\t\t\t  3>  Return                                 *")
        print("\t\t\t**********************************************************************")

        print("")
        choose = int(input("Enter your choice\n"))
        print("")

        if (choose == 1):
            display_user()

        elif(choose == 2):
            update_user()
            
        elif(choose == 3):
            break

        else:
            print("Wrong Choice, Please enter values between 1-3")




#_main_

x = check_connection()

if (x == 1):
    create_database()
    create_table()
    
else:
    print("Kindly check connection")



a = 'yes'

while(a == 'yes'):

    print("")
    print("")

    print("\t\t\t**********************************************************************")
    print("\t\t\t*\t\t\tGas Billing System                           *")
    print("\t\t\t*\t\t\t                                             *")
    print("\t\t\t*\t\t\t  1>  Admin                                  *")
    print("\t\t\t*\t\t\t  2>  User                                   *")
    print("\t\t\t*\t\t\t  3>  Exit                                   *")
    print("\t\t\t**********************************************************************")

    print("")
    choice = int(input("Enter your choice\n"))

    if(choice == 1):
        admin()

    elif(choice == 2):
        user()

    elif(choice == 3):
        break

    else:
        print("\nWrong Choice, Please enter values between 1-3")



    while (True):
        
        a = input("\nWish to continue ?\n")
    
        if (a == 'yes' or a == 'Yes' or a == 'no' or a == 'No'):
            break
            
        else:
            print("\nEnter correct value")



