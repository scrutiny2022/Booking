import copy
class Bookings:
    def __init__(self,dining_date):
        self.dining_date = dining_date
    def Book(self,i):
        print("Added Booking.The ticket code for " + self.dining_date +" is " + str(i))

def ListBookings(inf):
        if len(inf) == 0:
            print("No booking")
            return
        else:
            print("Bookings")
            #print(len(inf))
            for i in range(0,len(inf)):
                print(inf[i]['name']+","+str(inf[i]['phone'])+","+str(inf[i]['date'])+
                      " ( Ticket "+str(inf[i]['ticket_code'])+"), "+str(inf[i]['number'])
                      +", "+inf[i]['status'])
            return

def AllocateTable(file,user,info,key,tablefile):
    """file是file.readline之后生成的字典，user是用户的输入,info和key用来得到用户在book这个日期的时候提供的人数number, tablefile是存储每天table availability的字典"""
    #把user_input[3],也就是用户期望分配到的桌子序号，分开来
    User_Anticipated=[]    #用户输入的桌子序号
    for item in user[3].split(" "):
        User_Anticipated.append(item)
    #print("User_anticipated : {} ".format(User_Anticipated))    
    seats=[]   #用户输入的桌子序号的总座位数，具体从file中获得
    for item in User_Anticipated:
        seats.append(file[item])
    #print("seats is : {} ".format(seats))
    #print("number of people is",int(info[key]['number']))
    a=[]
    for i in User_Anticipated:
        if tablefile[user[1]][i] == "Available":
            a.append(tablefile[user[1]][i])
    #print("here is the inserting line")
    #print(len(a))
    #print(a)
    if len(User_Anticipated) > len(a):
        print("One or more tables are not available")
    elif info[key]['status'] != "Pending":
        print("Errors: table(s) already allocated to this booking.")
    else:
        if str(User_Anticipated[0]) in file and sum(seats) >= int(info[key]['number']):
            print("Allocated table {} to {} (Ticket {}).".format(user[3],user[1],user[2]))
            return True
        elif sum(seats) < int(info[key]['number']):
            print("Not enough seats are available. You may try to book another day.")
        else:
            pass

def ListTableAllocation(date,date_status,default_table_status):
    if date_status.get(date) == None:
        for i in range(1,8):
            print("0{}: {}".format(str(i),default_table_status.get("0"+str(i))))
        return True
    else:
        value=date_status[date]
        for i in range(1,8):
            print("0{}: {}".format(str(i),value.get("0"+str(i))))
    

#==========主函数============
print("Table file:")
string=input()
print("import {} tables".format(len(open(string).readlines())))
#===========分割线===========
answer=input()
date_dict={}  #创建一个字典，用来储存 date:ticket code
title=["name","phone","date","number","ticket_code","status"]
information=[]  #存储每一条订单的所有信息， listbooking函数会用到
Ls_Allo={}    #用来更新status,也就是allocated table  格式为--('日期','ticket_code'):infor_dict
date_table_status={}  #用来储存每一天的table的状态，方便更新
TS=["Available"]*7
TS3=["07","06","05","04","03","02","01"]
TS3.reverse()
TS1={TS3:TS for TS3,TS in zip(TS3,TS)}


#把file1.txt改成字典的形式，方便后续的判断
with open("file1.txt","r") as new:
    c=new.readlines()
ls=[]  #这只是一个中间过度的列表
for item in c:
    ls.append(item.split(" "))
number_of_seats=[]
table_number=[]
for i in ls:
    number_of_seats.append(int(i[2]))
    table_number.append(i[0])
tablefile={table_number:number_of_seats for table_number,number_of_seats in zip(table_number,number_of_seats)}
#以上部分的代码，把file1.txt转成了dictionary的格式，名为tablefile

while (answer != "Exit"):
    user = answer.split("|")
    user_input=[]
    for item in user:
        user_input.append(item.strip())
    if ( user_input[0] == "Book" ):
        bookings = Bookings(user_input[3])
        TS1={TS3:TS for TS3,TS in zip(TS3,TS)}
        #print("default table status is {}".format(TS1))
        if date_dict.get(user_input[3]) == None :   #判断输入的日期是不是一个新日期
            i=1
            date_dict[user_input[3]]=i
            date_table_status[user_input[3]]=TS1
        else:
            date_dict[user_input[3]]=1+date_dict[user_input[3]]
            i=date_dict[user_input[3]]
        #print(date_table_status)
        bookings.Book(i)
        infor_dict={title:user_input for title,user_input in zip(title,user_input[1:5])}
        """infor_dict这个字典，key:value 就是属性:输入的内容，每次新的booking输入都会更新，然后加进
        information这个列表里"""
        infor_dict['ticket_code']=i
        infor_dict['status']="Pending"
        information.append(infor_dict)
        key=tuple([user_input[3],str(i)])
        Ls_Allo[key]=infor_dict
        #print(Ls_Allo)
    if ( user_input[0] == "ListBookings" ):
        ListBookings(information)
    if ( user_input[0] == "Allocatetable" ):
        user_input_key=tuple(user_input[1:3])
        #print(user_input_key)
        #print(user_input[1])
        #print(date_table_status[user_input[1]])
        if ( AllocateTable(tablefile,user_input,Ls_Allo,user_input_key,date_table_status) ):
            if Ls_Allo.get('user_input_key') != "None":
                Ls_Allo[user_input_key]['status']="Allocated table:"+user_input[3]
            User_Anticipated=[]    #用户输入的桌子序号
            for item in user_input[3].split(" "):
                User_Anticipated.append(item)
            for item in User_Anticipated:
                date_table_status[user_input[1]][item]=Ls_Allo[user_input_key]['ticket_code']
            else:
                pass
    if ( user_input[0] == "ListTableAllocation" ):
        ListTableAllocation(user_input[1],date_table_status,TS1)
    answer = input()
    
print("Bye")


