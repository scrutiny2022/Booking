import openpyxl
import pandas as pd

"""my=pd.read_csv(r"D:\booking_red.txt")
print(my.head())
print("===============")
print(my)
print(my.columns)
print(my.index)
infor=my.loc[1]
print(type(infor))
for i in range(0,4):
    infor=my.loc[i]
    print(infor['name']+","+str(infor['phone'])+","+str(infor['date'])+
          "(),"+str(infor['number'])+", Allocated table: None")
"""
TS={'01':'Available','02':'Available','03':'Available','04':'Available',
    '05':'Available','06':'Available','07':'Available'}
TS1=["Available"]*7
TS3=[i for i in range(7,0,-1)]
print(TS3)
TS3.reverse()
TS2={TS3:TS1 for TS3,TS1 in zip(TS3,TS1) }
print(TS2)
