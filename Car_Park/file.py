import mysql.connector
import sys
from datetime import datetime


mydb = mysql.connector.connect(
    host="localhost", user="root",
    passwd="castro03", database="restDB")
def adminSum():

    adminSumBean = mydb.cursor()
    query = "SELECT ROUND(SUM(timedelta*1.5),2)" \
            " From Admin WHERE DAY(CarEntryDate) = DAY(NOW())"
    adminSumBean.execute(query)
    myresult = adminSumBean.fetchall()
    for x in myresult:
        print("Total Daily Takings:",x[0])
    mydb.commit()
def adminCount():
    mycursor = mydb.cursor()
    sql = "SELECT COUNT(timedelta) FROM Admin"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    print("Number of cars that have used the car park: ",myresult[0][0])
def adminAverageCharge():
    adminBean = mydb.cursor()
    query = "SELECT ROUND(AVG(timedelta*1.5),2) FROM Admin"
    adminBean.execute(query)
    myresult = adminBean.fetchall()
    for x in myresult:
        print("Average Charge Per Car:",x[0])
    mydb.commit()
def adminAverageStay():
    adminSession = mydb.cursor()
    query = "SELECT ROUND(AVG(timedelta),2) FROM Admin"
    adminSession.execute(query)
    myresult = adminSession.fetchall()
    for x in myresult:
        print("Average Length of stay per car:",x[0],"hours")
    mydb.commit()
def admin():
    adminSum()
    adminCount()
    adminAverageCharge()
    adminAverageStay()

def updateAdmin(timedelta):
    adminSession = mydb.cursor()
    query = "INSERT INTO Admin (timedelta) VALUES (%d)"

    sql = query % timedelta
    adminSession.execute(sql)
    mydb.commit()
def updateup():
    exitSession = mydb.cursor()
    current_spaces = selectspaces()
    savedtuple = (current_spaces+1,current_spaces)
    sql = "UPDATE Free_Spaces SET spaces = %s WHERE spaces = %s"

    exitSession.execute(sql,savedtuple)
    mydb.commit()
    print("There are now",current_spaces+1,"free spaces")
def carleave():
    try:
        ticketnum = input("Enter your ticket number:\n")
        time = datetime.now()
        hour=time.strftime("%H")
        sqlcursor = mydb.cursor()
        sql = "SELECT Entry_Time FROM CarEntry WHERE TicketNumber = %d"
        query = sql % int(ticketnum)
        sqlcursor.execute(query)
        result = sqlcursor.fetchall()
        entry_time = result[0][0]
        sql1 = "DELETE FROM CarEntry WHERE TicketNumber = %d"
        query2 = sql1 % int(ticketnum)
        sqlcursor.execute(query2)
        mydb.commit()
        print("Record has been deleted")
        print("Arrived at",entry_time )
        print("Leaving at:", hour)
        print("\n\tParked for:",int(int(hour)-int(entry_time)))
        timedeltat = int(int(hour)-int(entry_time))
        updateAdmin(timedeltat)
        if int(hour)-int(entry_time) == 0:
            print("You do not have to pay!")
        else:
            print("You have to pay: $",(1.50*timedeltat))
    except IndexError:
        print("Your Ticket Number is not yet registered.")
        sys.exit()

def updatespaces():
    mycursor = mydb.cursor()
    sql = "SELECT * FROM Free_Spaces"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    freespaces = int(myresult[0][0])
    update = "UPDATE Free_Spaces SET spaces = %s WHERE spaces = %s"
    indexes = (freespaces - 1, freespaces)
    mycursor.execute(update, indexes)

    print("Free Spaces Updated\n\tThere are now", indexes[0], "spaces")
    mydb.commit()

def newcar():
    current_time = datetime.now()
    time_hour = current_time.strftime("%H")
    freespaces = selectspaces()
    mycursor = mydb.cursor()
    sql = "INSERT INTO CarEntry (Entry_Time, TicketNumber) VALUES (%s, %s)"
    val = (time_hour, freespaces)
    mycursor.execute(sql, val)
    mydb.commit()
    print("\t\tYour ticket number is",freespaces)
def selectspaces():
    mycursor = mydb.cursor()
    sql = "SELECT * FROM Free_Spaces"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    freespaces = int(myresult[0][0])
    mydb.commit()
    return freespaces


user = input("Admin or Client?\n")
if user == "Client" or user == "c":
    welcome = input("Entry or Exit\n")
    if welcome == "Entry" or welcome == "e":
        print("There are", selectspaces(), "free spaces")
        accept = input("Go in?\n[Yes/No]\n")

        if accept == "Yes" or accept == "y":
            if selectspaces() > 0:
                newcar()
                updatespaces()
                print("You may go in now...")
            elif selectspaces() <= 0:
                print("We are very sorry there are no more free spaces left")

        if accept == "No" or "n":
            sys.exit()
        else:
            print("Enter a correct value")
    elif welcome == "Exit" or welcome == "x":
        carleave()
        updateup()
    else:
        print("Enter a correct value")
elif user == "Admin" or user == "a":
    admin()