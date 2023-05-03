import mysql.connector
import pandas as pd

#Connect to mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)
mycursor = mydb.cursor()

#Create the DB (if not already exists)
mycursor.execute("CREATE DATABASE IF NOT EXISTS Netflix_Originals")

#Create the table for the csv data (if not exists)
mycursor.execute("""
  CREATE TABLE IF NOT EXISTS Netflix_Originals.Netflix_Unit (
    ID int NOT NULL AUTO_INCREMENT PRIMARY KEY ,
    Title varchar (100)  NOT NULL,
    Genre varchar (60)  NOT NULL,
    Language varchar (15)  NOT NULL, 
    Runtime int  NOT NULL, 
    Score float NOT NULL ,
    Immagine varchar (100) NOT NULL 
  );""")

#Delete data from the table Clsh_Unit
mycursor.execute("DELETE FROM Netflix_Originals.Netflix_Unit")
mydb.commit()

#Read data from a csv file
Netflix_data = pd.read_csv('./Netflix_Db.csv', index_col=False, delimiter = ',')
Netflix_data = Netflix_data.fillna('Null')
print(Netflix_data.head(20))

#Fill the table
for i,row in Netflix_data.iterrows():
    cursor = mydb.cursor()
    #here %S means string values 
    sql = "INSERT INTO Netflix_Originals.Netflix_Unit VALUES (%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, tuple(row))
    print("Record inserted")
    # the connection is not auto committed by default, so we must commit to save our changes
    mydb.commit()

#Check if the table has been filled
mycursor.execute("SELECT * FROM Netflix_Originals.Netflix_Unit")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)