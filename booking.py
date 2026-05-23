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
class BookingSystem:
    def __init__(self):
        self.__bookList = []  #已经预定的信息,[bookInfo-1,bookInfo-2] private variable
        self.__dailyTableStatus:dict[str, int] = {}
        self.bookDict:dict[str,int] = {}
    def findBookInfo(self,date,**kwargs):
        filtered = [item for item in self.__bookList if item.date == date]
        if 'ticket_code' in kwargs:
            ticket_code = kwargs['ticket_code']
            for item in filtered:
                if item.code == ticket_code:   # 注意是 ==
                    return item
        elif 'name' in kwargs and 'phone' in kwargs:
            name = kwargs['name']
            phone = kwargs['phone']
            for item in filtered:
                if item.name == name and item.phone == phone:
                    return item
            return None
    
    def book(self,name,date,phone):
        if self.bookDict.get(date,None): #you wen ti
            self.bookDict[date] += 1
        else:
            self.bookDict[date] = 1
        code = self.bookDict[date]
        table = 0
        print(f"Booking successful. Your ticket code is {date}--{code}.")
        bookInfo = BookInfo(name,date,phone,code,table)
        self.__bookList.append(bookInfo)
        #update the table status and date table status for the booking
        if self.__dailyTableStatus.get(date,None) == None:
            self.__dailyTableStatus[date] = "0000000"
        else:
            pass
        return None
    def allocate(self,name,date,phone):
        string = int(self.__dailyTableStatus[date])
        booking = self.findBookInfo(date,name = name,phone=phone)
        for e in range(7):
            if not (string & (1 << (6-e))):
                string |= (1<<(6-e))
                booking.table = e+1
                break
            else:
                pass
        self.__dailyTableStatus[date] = bin(string).replace('0b','')
        print(f"Allocate successfully. {date} code {booking.code} has table {booking.table}")
        pass
    def listing(self):
        for e in self.__bookList:
            print(e)
        return None
    


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

    return None

#Booking|Name|Date|Contact number| number of people
#Allocate|Date|Ticket code|Name
if __name__ == '__main__':
    Init()
    a = "Book|Leo|2025-07-01|12345678|4"
    b = a.split('|')
    BookingSys = BookingSystem()
    BookingSys.book(b[1],b[2],b[3])
    a = "Book|Leon|2025-07-01|1234|4"
    b = a.split('|')
    BookingSys.book(b[1],b[2],b[3])
    a = "Book|Leo|2025-07-03|12345678|4"
    b = a.split('|')
    BookingSys.book(b[1],b[2],b[3])
    a = "Allocate|Leon|2025-07-01|1234|4"
    b = a.split('|')
    BookingSys.allocate(b[1],b[2],b[3])
