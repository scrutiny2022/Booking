import os
import pandas as pd
import openpyxl

class Bookings:
    def __init__(self,contact_name,phone_number,dining_date,number_of_seat):
        self.contact_name = contact_name
        self.phone_number = phone_number
        self.dining_date = dining_date
        self.number_of_seat = number_of_seat
    def Book(self,i):
        print("Added Booking.The ticket code for " + self.dining_date +" is " + str(i))

def Checkin(user_input,i):   #把顾客的信息写入一个文件中
    with open("C:\\Users\\Leo\\Desktop\\booking_red.txt","a") as my_file:
        for i in range(1,4):
            my_file.write(user_input[i])
            my_file.write(",")
        my_file.write(user_input[4])
        my_file.write("\n")
    my_file.close()

def Exit():
    #退出
    print("Bye")

def ListBookings():
    pass


def Run():
    answer=input()
    date_dict={}  #创建一个字典，用来储存 date:ticket code
    ticket_code=1
    while (answer != "Exit"):
        user = answer.split("|")
        user_input=[]
        for item in user:
            user_input.append(item.strip())
        if ( user_input[0] == "Book" ):
            bookings = Bookings(user_input[1],user_input[2],user_input[3],user_input[4])
            if date_dict.get(user_input[3]) == None :   #判断输入的日期是不是一个新日期
                ticket_code=1
                date_dict[user_input[3]]=ticket_code
            else:
                date_dict[user_input[3]]=1+date_dict[user_input[3]]
                ticket_code=date_dict[user_input[3]]
            Checkin(user_input,ticket_code)
            bookings.Book(ticket_code)
        if ( user_input[0] == "ListBookings" ):
            pass
        if ( user_input[0] == "Allocatetable" ):
            pass
        answer=input()
    Exit()
"""============我是一条分界线============"""
with open("C:\\Users\\Leo\\Desktop\\booking_red.txt","w+") as my_file:
    my_file.write("name,phone,date,number\n")
Run()

