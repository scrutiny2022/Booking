class Bookings:
    def __init__(self,contact_name,phone_number,dining_date,number_of_seat):
        self.contact_name = contact_name
        self.phone_number = phone_number
        self.dining_date = dining_date
        self.number_of_seat = number_of_seat
    def Book(self,i):
        print("Added Booking.The ticket code for " + self.dining_date +" is " + str(i))
def ListBookings(inf):
    if len(inf) == 0:
        print("No booking")
    else:
        print("Bookings")
        #print(len(inf))
        for i in range(0,len(inf)):
            print(inf[i]['name']+","+str(inf[i]['phone'])+","+str(inf[i]['date'])+
                  " ( Ticket "+str(inf[i]['ticket_code'])+"), "+str(inf[i]['number'])
                  +", Allocated table: "+inf[i]['status'])

def AllocateTable(file,user):
    if str(user[3]+"\n") in file:
        print("Allocated table {} to {} (Ticket {}).".format(user[3],user[1],user[2]))
        return True
    else:
        print("Error: Table not found")
def Exit():
        print("Bye")

#==========主函数============
print("Table file:")
answer=input()
date_dict={}  #创建一个字典，用来储存 date:ticket code
i=1
title=["name","phone","date","number","ticket_code","status"]
information=[]
tablefile=[]
Ls_Allo={}    #用来更新status,也就是allocated table
while (answer != "Exit"):
    user = answer.split("|")
    user_input=[]
    for item in user:
        user_input.append(item.strip())
    if ( user_input[0] == "Book" ):
        bookings = Bookings(user_input[1],user_input[2],user_input[3],user_input[4])
        if date_dict.get(user_input[3]) == None :   #判断输入的日期是不是一个新日期
            i=1
            date_dict[user_input[3]]=i
        else:
            date_dict[user_input[3]]=1+date_dict[user_input[3]]
            i=date_dict[user_input[3]]
        bookings.Book(i)
        infor_dict={title:user_input for title,user_input in zip(title,user_input[1:5])}
        """infor_dict这个字典，key:value就是属性:输入的内容，每次新的booking输入都会更新，然后加进
        information这个列表里"""
        infor_dict['ticket_code']=i
        infor_dict['status']="None"
        information.append(infor_dict)
        key=tuple([user_input[3],str(i)])
        Ls_Allo[key]=infor_dict
        #print(Ls_Allo)
    if ( user_input[0] == "ListBookings" ):
        ListBookings(information)
    if ( user_input[0] == "Allocatetable" ):
        user_input_key=tuple(user_input[1:3])
        #print(user_input_key)
        with open("C:\\Users\\Leo\\Desktop\\tablefile.txt","r") as new:
            tablefile=new.readlines()
        #print(tablefile)
        if ( AllocateTable(tablefile,user_input) ):
            if Ls_Allo.get('user_input_key') != "None":
                Ls_Allo[user_input_key]['status']=user_input[3]
            else:
                pass
    if ( user_input[0] == "tablefile.txt" ):
        with open("C:\\Users\\Leo\\Desktop\\tablefile.txt","r") as new:
            tablefile=new.readlines()
        #print(tablefile)
        print("import {} tables".format(len(tablefile)))
    answer = input()
Exit()


