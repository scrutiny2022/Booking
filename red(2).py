"""infor=[]
title=["name","phone","date","number","ticket_code","status"]
inf=["CKo","1234","22-04-2022","5","1","None"]
infor_dict={title:inf for title, inf in zip(title,inf)}
print(infor_dict)
print("===============")
book1={"name":"CK","phone":"1234","date":"22-04-2022","number":"5"}
infor.append(book1)
print(book1)
print(infor)
book2={"name":"Le","phone":"1234","date":"22-05-2022","number":"5"}
infor.append(book2)
print(infor)
print(infor[0]["name"])
print("\n")
print("\n")"""

print("main part")
answer=input()
title=["name","phone","date","number","ticket_code","status"]
infor=[]
i=0
infor_dict={}
while answer != "Exit":
    user=answer.split("|")
    user_input=[]
    for item in user:
        user_input.append(item.strip())
    infor_dict={title:user_input for title,user_input in zip(title,user_input[0:3])}
    print(infor_dict)
    infor.append(infor_dict)
    infor[i]['ticket_code']=4
    print(infor)
    i=i+1
    answer=input()
print("Bye")
print(infor_dict)
print(len(infor))
