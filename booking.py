from dataclasses import dataclass
table:dict = {} #饭店桌子的信息,{'01': 2, '02': 2... '07': 6}桌号:每桌座位
bookdict:dict={} #每日票号,{'2025-07-01': 1, '2025-07-07': 1}
Input:list = [] #
bookList:list = [] #已经预定的信息,[bookInfo-1,bookInfo-2]
status:dict = {} #{'01': 'available', '02': 'available'...'07': 'available'}桌子是否被预定
dailyTableStatus:dict = {}
@dataclass
class BookInfo:
    name:str
    date:str
    phone:int
    code:int #ticket code
    table:int
    def __str__(self):
        return f"{self.table}|{self.name}|{self.phone}|{self.date}|{self.code}"

class Mybooking:
    def __init__(self,info:BookInfo):
        self.info = info
    def __str__(self):
        return f"The ticket code for {self.info.date} is {self.info.code}"
    def update(self):
        #get and update ticket code in the booking dictionary
        if bookdict.get(self.info.date,None): #you wen ti
            bookdict[self.info.date] += 1
        else:
            bookdict[self.info.date] = 1
        self.info.code = bookdict[self.info.date]
        print(f"Booking successful. Your ticket code is {self.info.date}--{self.info.code}.")
        None

def findBookInfo(bookinfoList:list, date:str,code:int):
    for i in bookinfoList:
        if i.date == date and i.code == code:
            return i
        else:
            pass
def Init():
    #读取饭店桌子的信息并存储在字典里
    with open("file1.txt","r") as new:
        tablefile=new.readlines()
    st = "0"*len(tablefile) # daily table status 0000000
    print("import {} tables".format(len(tablefile)))
    for i in tablefile:
        a = i.strip().split(" ")
        table[a[0]] = int(a[-1])
        status[a[0]] = "Available"
    return None
def Booking(Input:list):
    #处理预定信息
    #Input:list= userInput.split('|')
    ticket_code = 0
    table = 0
    bookInfo = BookInfo(Input[1],Input[2],Input[3],ticket_code,table)
    bookList.append(bookInfo)
    mybook = Mybooking(bookInfo)
    #update the table status and date table status for the booking
    if dailyTableStatus.get(bookInfo.date,None) == None:
        dailyTableStatus[bookInfo.date] = "0000000"
    else:
        pass
    mybook.update()
    return None

def Allocation(info:BookInfo):
    #根据日期及ticket code分配桌子，不考虑人数和座位数
    string = int(dailyTableStatus[info.date])
    for e in range(7):
        if not (string & (1 << (6-e))):
            string |= (1 << (6-e))
            info.table = e+1
            break
        else:
            pass
    dailyTableStatus[info.date] = bin(string).replace('0b','')
    print(f"Allocate successfully. {info.date} code {info.code} on Table {info.table}")
    return None
def Listing():
    #List all the tables that have been booked
    #table number | who booked | Contact number| Date
    if bookList == []:
        print("No Booking")
        return
    for i in bookList:
        print(i)
    return None
def Removing(bookinfoList:list, date:str,code:int):
    for i in bookinfoList:
        if i.date == date and i.code == code:
            if i.table == 0:
                pass
            e = int(i.table) - 1 #如果未分配桌子，会出问题
            string = int(dailyTableStatus[i.date])
            string |= (1 << (6-e))
            dailyTableStatus[i.date] = bin(string).replace('0b','')
            bookinfoList.remove(i)
        else:
            pass
    
    return None
def Rule():
    #Booking|Name|Date|Contact number| number of people
    #Allocate|Date|Ticket code|Name
    while True:
        userInput = input()
        if userInput == "Exit":
            print("bye")
            break
        Input = userInput.split('|')
        if Input[0] == "Booking":
            Booking(Input)
            pass
        if Input[0] == "Allocate":
            allocate = findBookInfo(bookList,Input[1],int(Input[2]))
            Allocation(allocate)
        if Input[0] == "List":
            Listing()
        if Input[0] == "Remove":
            remove = Removing(bookList,Input[1],int(Input[2]))
            print(bookList)
            print(dailyTableStatus)
    return None

#Booking|Name|Date|Contact number| number of people
#Allocate|Date|Ticket code|Name
if __name__ == '__main__':
    Init()
    Rule()
