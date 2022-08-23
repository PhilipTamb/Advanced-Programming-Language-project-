import mysql.connector


try:
  connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="instafix"
  )

  cursor = connection.cursor()

except mysql.connector.Error as error:
    print("Failed to insert record into Laptop table {}".format(error))


try: 
  cursor.execute("SELECT * FROM professionisti")
  connection.commit()

except mysql.connector.Error as error:
    print("Failed to insert record into Laptop table {}".format(error))

finally:
    myresult = connection.fetchall()
    for x in myresult:
      print(x)
    cursor.close()


if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")







