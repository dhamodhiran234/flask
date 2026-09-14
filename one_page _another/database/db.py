import mysql.connector
from mysql.connector import Error

try:
    # Attempt to connect to the database
    dbcon = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Dhamo@123#Db",
        database="fla",
        auth_plugin="mysql_native_password"  # Add if needed for auth issues
    )

    if dbcon.is_connected():
        print("Database connection successful!")
        
        # Create cursor only after a successful connection
        cursor = dbcon.cursor()
        
        # 2. Define SQL INSERT query using placeholders (%s)
        sql_query = "INSERT INTO stu (name, age) VALUES (%s, %s)"
        
        # 3. Define the values to insert
        values = ("Dhamo", 25)

        # 4. Execute the query
        cursor.execute(sql_query, values)

        # 5. COMMIT the transaction (required for INSERT, UPDATE, DELETE)
        dbcon.commit()

        print(f"Record inserted successfully! Row ID: {cursor.lastrowid}")

except Error as e:
    # Catch any MySQL connection or execution errors
    print(f"Error connecting to MySQL: {e}")

finally:
    # Safely close the connection if it was established
    if 'dbcon' in locals() and dbcon.is_connected():
        cursor.close()
        dbcon.close()
        print("MySQL connection is closed.")