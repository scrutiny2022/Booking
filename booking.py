from dataclasses import dataclass
table:dict = {} #饭店桌子的信息,{'01': 2, '02': 2... '07': 6}桌号:每桌座位
bookdict:dict={} #已经预定的信息,{'2025-07-01': 1, '2025-07-07': 1}
Input:list = [] #
status:dict = {} #{'01': 'available', '02': 'available'...'07': 'available'}桌子是否被预定
@dataclass
class BookInfo:
    name:str
    phone:int
    date:str
    code:int #ticket code
    def __str__(self):
        return f"Added booking. The ticket code for {self.date} is {self.code}"
class Mybooking:
    def __init__(self,info:BookInfo):
        self.info = BookInfo
    def __str__(self):
        return str(self.info)
    def update(self):
        None
    
def Init():
    #读取饭店桌子的信息并存储在字典里
    with open("file1.txt","r") as new:
        tablefile=new.readlines()
    for i in tablefile:
        a = i.strip().split(" ")
        table[a[0]] = int(a[-1])
        status[a[0]] = "Available"
    return None
def Booking(Input:list):
    #预定信息
    if bookdict.get(Input[2],None):
        bookdict[Input[2]] += 1
    else:
        bookdict[Input[2]] = 1
    Input.append(bookdict[Input[2]])
    Allocation()#try to allocate table(s) for the booking
    return None
def Allocation():
    return None
def Listing():
    #List all the tables that have been booked
    #table number | who booked | Contact number| Date
    return None
def Removing():
    return None
def Rule():
    if userInput == "Exit":
        print("bye")
        return
    
    return None

#Booking|Name|Date|Contact number| number of people
if __name__ == '__main__':
    Init()
    print(table,status)
    userInput = "Booking|L|2025-07-01|134|4"
    ls:list= userInput.split('|')
    print(ls)
    Booking(ls)
    userInput = "Booking|Leo|2025-07-07|134|4"
    ls:list= userInput.split('|')
    Booking(ls)
    print(bookdict)
    Rule()
