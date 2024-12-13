import pandas as pd
import numpy as np
import mysql.connector as m
import matplotlib.pyplot as plt

con=m.connect(host="localhost",user="root",passwd="gajabdin22",database="buses")
cursor=con.cursor(prepared=True)
print("""""_________________________________________________
           WELCOME TO BUS TICKET RESERVATION (BTR BOOKS)
__________________________________________________________________
_____________________________________________________________________________
""""")

 
while True :
        choice=input("Do you want to:\n A)Login/Signup.\n B)Book bus tickets. \n C)Cancel tickets. \n D)Check Your bookings.  \n E)Admin \n F)Help  \n G)Talk to MITI, our AI agent :")
        if choice=="A":

                    print("Taking you to the login window")
                    Pname=(input("Enter your name"))
                    pin=int(input("Enter the last 4 digits of your phone number"))
                    user=("INSERT INTO users VALUES ('%s',%s)"%(Pname,pin))
                    cursor.execute(user)
                    con.commit()
                    print("LOGGED IN")
                    print("""""""THANKYOU FOR VISITING OUR BUS WEBSITE""""""""")
        elif choice=="B":
                    print("Let's look for a safe journey")
                    name=(input("Enter your name"))
                    phone=int(input("Enter the last 4 digits of your phone number"))
                    x=(input("Leaving from"))
                    y=(input("Going to"))
                    date=(input("DATE OF JOURNEY"))
                    depart=(input("DATE OF RETURN"))
                    print("Data entered successfully")
                    ch=input("\n L)LATER BOOKINGS  \n T)TATKAL BOOKINGS :")
                    print("These are the buses options for you")
                    if ch=="L":
                        cursor.execute("SELECT*FROM BUS WHERE Startfrom=('%s') and destination=('%s')"%(x,y))
                        data=cursor.fetchall()
                        print(data)
                        bus=input("Enter the busid of the bus you want to travel on")
                        cursor.execute("INSERT INTO book_ticket(Name,phone,come,goto,arrive,depart,BUSid)VALUES('%s',%s,'%s','%s',%s,%s,%s)"%(name,phone,x,y,date,depart,bus))
            
                        con.commit()
                        print("TICKET locked SUCCESSFULLY")
                        print("Proceed to payment options")
                        Pay=input("Select payment options \n A)Pay online using debit/UPI \n B)Pay cash while travelling")
                        if Pay=="A":
                            UPI=int(input("ENTER YOUR PHONE NUMBER.\n Please accept our payment request to your contact"))
                        elif Pay=="B":
                            print("Your seat is locked. Be on time.YOUR SEAT will be alotted to other passenger on the next stop if your payment remains unfinished.\n We will be waiting for you.")
                        print("Ticket booked successfully")
                        print("""""""THANKYOU FOR VISITING OUR BUS WEBSITE""""""""")
                    elif ch=="T":
                        cursor.execute("SELECT*FROM BUS WHERE Startfrom=('%s') and destination =('%s')"%(x,y))
                        data=cursor.fetchall()
                        print(data)
                        bus=int(input("Enter the busid of the bus you want to travel on"))
                        cursor.execute("INSERT INTO book_ticket(Name,phone,come,goto,arrive,depart,BUSid)VALUES('%s',%s,'%s','%s',%s,%s,%s)"%(name,phone,x,y,date,depart,bus))
                        con.commit()
                        print("TICKET locked SUCCESSFULLY")
                        print("Proceed to payment options")
                        Pay=input("Select payment options \n A)Pay cash while travelling")
                        print("Your seat is locked. Be on time.YOUR SEAT will be alotted to other passenger on the next stop if your payment remains unfinished.\n We will be waiting for you.")
                        print("""""""THANKYOU FOR VISITING OUR BUS WEBSITE""""""""") 
            
        elif choice=="C":
                   
                   print("Take Care.We hope that you continue your journey later.")
                   name=input("Enter your name")
                   pin=input("Enter your last 4 digits of phone number")
                   x=input("Leaving from")
                   dele=("Delete from book_ticket WHERE Name= ('%s') and Phone=(%s)"%(name,pin))
                   cursor.execute(dele)
                   con.commit()
                   print("we have deleted your bookings")
                   print("""""""THANKYOU FOR VISITING OUR BUS WEBSITE""""""""")
        elif choice=="D":
                    
                   print("Let's figure out your bookings")
                   name=input("Enter your name")
                   pin=input("Enter the 4 digit pin")
                   cursor.execute("select* from book_ticket where Name=('%s') and Phone=(%s)"%(name,pin))
                   data=cursor.fetchall()
                   print("Here is your bus id. Use it to know your bus details")
                   print(data)
                   print("To know your bus timings and name please enter your bus id")
                   bus=int(input())
                   cursor.execute("select*from bus where BUSid=(%s)"%(bus))
                   data=cursor.fetchall()
                   print(data)
                   print("We hope you are satisfied with the results")
                   print("""""""THANKYOU FOR VISITING OUR BUS WEBSITE""""""""")
        elif choice=="F":
                   print("We are sorry for the inconvenience.Write your issue to us at btrbooks@gmail.com")
        elif choice=="E":
                   print("Welcome to Admin hosts")
                   login=int(input("ENTER ADMIN LOGIN KEY"))
                   Passwd=input("Enter admin login Password")
                   if login==5489:
                       choice=input("Do you want to \n A)ADD new bus details B)Analyse bus details C)Update Bus details")
                       if choice=="A":
                           x=int(input("ENTER BUSid"))
                           y=input("Enter Bus name")
                           z=input("Enter starting point")
                           w=input("Enter destination")
                           p=input("Enter arrival time in format '12:00 AM/PM'")
                           q=input("Enter departure time in format'12:00 AM/PM'")
                           r=int(input("Enter Bus charge per customer"))
                           cursor.execute("INSERT INTO BUS(BUSid,busname,Startfrom,Destination,arrivaltime,departuretime,busnumber) VALUES(%s,'%s','%s','%s','%s','%s',%s)"%(x,y,z,w,p,q,r))
                           con.commit()
                           print("Bus data submitted")
                           print("""""""THANKYOU FOR VISITING OUR BUS WEBSITE""""""""")
                       elif choice=="B":
                           x=int(input("Enter busid"))
                               
                           option=input("What do you want to analyse \n 1)count booked tickets \n 2)Help")
                           if option=='1':
                               
                               cursor.execute("SELECT count(Name) from book_ticket where BUSid=(%s)"%(x))
                               data=cursor.fetchall()
                               print(data)
                               x=pd.read_sql(("SELECT*FROM BOOK_TICKET where BUSid=(%s)"%(x)),con)


                               print(x)
                               print("""""""THANKYOU FOR VISITING OUR BUS WEBSITE""""""""")
                               
                           elif option=='2':
                               print("Please enter the following details.")
                               z=input("Enter your contact number")
                               a1=input("Enter your name")
                               issue=input("Enter issue in one word so that our experts can come up with solutions")
                               cursor.execute("INSERT INTO BUSADMINS( NAME,PHONE,ISSUE)VALUES('%s',%s,'%s')"%(z,a1,issue))
                               con.commit()
                               print("We will contact you soon. Until than enjoy our features of data analysis")
                               print("""""""THANKYOU FOR VISITING OUR BUS WEBSITE""""""""")
                               
                               
                               
                               
                       elif choice=="C":
                               print("Lets see how we can help you update the timings.")
                        
                               d=input("Enter Busid to which the timings are to be changed")
                               e=input("ENTER new bus arrival timings")
                               f=input("Enter new bus departure timings")
                               print("BUS DETAILS UPDATED")
                               cursor.execute("UPDATE bus set arrivaltime='%s'where busid=%s"%(e,d))
                               con.commit()
                               cursor.execute("UPDATE BUS SET departuretime='%s' where bus id=%s"%(f,d))#doubt
                               con.commit()
                               print("BUS DETAILS UPDATED")
                               print("""""""THANKYOU FOR VISITING OUR BUS WEBSITE""""""""")
        elif choice=="G":
                print("Hey there I am Miti, an AI agent. I will help you find best tours if you are late to catch your booked tickets.")
                z=input("Enter your busid")
                m=input("Enter your name")
                now=input("Where are you now")
                go=input("Where do you want to go")
                cursor.execute("select*from bus where startfrom='%s'and destination='%s'"%(now,go))
                data=cursor.fetchall()
                print(data)
                print("Nice to meet you",m)
                print("Just pay Rs.99 extra now and here are some food items which you will get for free during your journey")
                cursor.execute("select*from book_food")
                print(cursor.fetchall())
                print("To pay enter bbrbook.com/book_food on your mobile web browser and decide what you desire to eat during your trip")
                print("Hope to meet you soon. I always enjoy talking to you",m)
                print("""""""THANKYOU FOR VISITING OUR BUS WEBSITE""""""""")

                               
                               

                               
                                              
   
                                          
                           
                       
                   
            





            
