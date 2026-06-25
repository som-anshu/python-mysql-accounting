import mysql.connector as a
import sys

# Establish Database Connection
try:
    mydb = a.connect(
        host='localhost',
        user='root',
        passwd='9713',  # Replace with your MySQL password
        database='account'
    )
    mycursor = mydb.cursor()
except a.Error as err:
    print(f"Error connecting to MySQL: {err}")
    sys.exit(1)

# Main Execution Loop
while True:
    print("""
    =========================================
                    MAIN MENU
    =========================================
    1. ADD DATA
    2. DELETE A RECORD
    3. MODIFY/UPDATE A RECORD
    4. SEE COMPLETE RECORD OF A CLIENT
    5. SEE RECORD OF A PARTICULAR DATE
    6. SEE ENTIRE DATA
    """)
    
    try:
        option = int(input("* OPTION: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    # 1. INSERT DATA INTO TABLE
    if option == 1:
        flag = True
        while flag:
            print("\n--- ADD NEW RECORD ---")
            invoice_no = input("INVOICE NUMBER: ")
            client = input("CLIENT NAME: ")
            billing_amount = float(input("NET TOTAL AMOUNT: "))
            Date = input("DATE (YYYY-MM-DD): ")
            
            data = (invoice_no, client, billing_amount, Date)
            query = "INSERT INTO record (invoice_no, client, billing_amount, Date) VALUES (%s, %s, %s, %s)"
            mycursor.execute(query, data)
            mydb.commit()
            
            opt = input("\nMORE DATA TO ADD? (Y/N): ")
            if opt in 'Nn':
                flag = False

    # 2. DELETE DATA FROM TABLE
    elif option == 2:
        flag = True
        while flag:
            print("\n--- DELETE RECORD ---")
            invoice_no = input("Enter the INVOICE NUMBER of the record you want to delete: ")
            query = "DELETE FROM record WHERE invoice_no = %s"
            mycursor.execute(query, (invoice_no,))
            mydb.commit()
            
            opt = input("\nMORE DATA TO DELETE? (Y/N): ")
            if opt in 'Nn':
                flag = False

    # 3. UPDATE DATA IN TABLE
    elif option == 3:
        flag = True
        while flag:
            print("\n--- UPDATE RECORD ---")
            invoice_no = input("Enter the INVOICE NUMBER of the record you want to UPDATE: ")
            
            print("""
            WHAT DO YOU WANT TO UPDATE:
            1. Client Name
            2. Billing Amount (Override)
            3. Billing Amount (Add/Subtract)
            4. Date
            """)
            choice = input("> ")

            if choice == '1':
                client = input("CORRECT CLIENT NAME: ")
                data = (client, invoice_no)
                mycursor.execute("UPDATE record SET client=%s WHERE invoice_no=%s", data)
            elif choice == '2':
                billing_amount = float(input("CORRECT BILLING AMOUNT: "))
                data = (billing_amount, invoice_no)
                mycursor.execute("UPDATE record SET billing_amount=%s WHERE invoice_no=%s", data)
            elif choice == '3':
                billing_amount = float(input("+ OR - BILLING AMOUNT: "))
                data = (billing_amount, invoice_no)
                mycursor.execute("UPDATE record SET billing_amount = billing_amount + %s WHERE invoice_no=%s", data)
            elif choice == '4':
                Date = input("CORRECT DATE (YYYY-MM-DD): ")
                data = (Date, invoice_no)
                mycursor.execute("UPDATE record SET Date=%s WHERE invoice_no=%s", data)
                
            mydb.commit()
            opt = input("\nMORE DATA TO UPDATE? (Y/N): ")
            if opt in 'Nn':
                flag = False

    # 4. PRINT ENTIRE DATA OF A SPECIFIC CLIENT
    elif option == 4:
        print("\n--- CLIENT FILTER ---")
        client = input("CLIENT NAME: ")
        mycursor.execute("SELECT * FROM record WHERE client=%s", (client,))
        print("\nDATA OF CLIENT:")
        for i in mycursor:
            print(i)

    # 5. PRINT RECORDS GENERATED ON A SPECIFIC DATE
    elif option == 5:
        print("\n--- DATE FILTER ---")
        Date = input("DATE (YYYY-MM-DD): ")
        mycursor.execute("SELECT * FROM record WHERE Date=%s", (Date,))
        print("\nDATA OF THIS DATE:")
        for i in mycursor:
            print(i)

    # 6. PRINT ENTIRE DATA TABLE
    elif option == 6:
        print("\n--- ENTIRE TABLE RECORDS ---")
        mycursor.execute("SELECT * FROM record")
        for i in mycursor:
            print(i)

    # NAVIGATION CONTROL MENU
    print("\n-----------------------------------------")
    print("1. MAIN MENU | 2. EXIT")
    try:
        nav_opt = int(input("> "))
        if nav_opt == 2:
            mycursor.close()
            mydb.close()
            print("Database connection closed. Exiting.")
            break
    except ValueError:
        print("Invalid Choice. Defaulting back to Main Menu.")
