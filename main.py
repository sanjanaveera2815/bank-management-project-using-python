import json
import random
import string
from pathlib import path
class Bank:
    dtabase='data.json'
    data=[]
    try:
        if path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("no such file exist ")
    except Exception as error:
        print(f"an expection occcured a {error}")
    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(Bank.data))
    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters,k = 3)
        num = random.choices(strings.digits,k= 3)
        spchar = random.choices("!@#$%^&*",k= 1)
        id = alpha + num + spchar
        random.shuttle(id)
        return "".join(id)

    def Createaccount(self):
        info = {
           "name": input("Tell your name :- "),
           "age": int(input("Tell your age :- ")),
           "email": input("Tell your email :- "),
           "pin": int(input("Tell your 4 number pin :- ")),
           "accountNo." : Bank.__accountgenerate(),
           "balance" : 0
        }
        if info['age'] < 18 or len(str(info ['pin'])) !=4:
           print("sorry you cannot create your account")
        else:
           print("account has been created successfully")
           for i in info:
               print(f"{i} : {info[i]}")
           print("please note down your account number")
           Bank.data.append(info)

           Bank.__update()
    def depositmoney(self):
        accnumber = input("please tell your account number")
        pin = int(input("please tell your pin aswell"))
        userdata = [i for i in Bank.data if i ['accountNo.' == accnumber and i['pin']== pin]]
        if userdata == False:
            print("sorry no data found")
        else:
            amount = int(input("how much you want to deposit "))
            if amount>10000 or amount < 0:
                print("sorry your amount is too much you can deposit below 10000 and above 0")
            else:
                userdata[0]['balance'] += amount
                Bank._update()
                print("Amount deposited successfully")
    def withdrawmoney(self):
        accnumber = input("please tell your acc number")
        pin = int(input("please tell your pin"))
        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]
        if userdata == False:
            print("sorry no data found")

        else:
            amount=int(input("how much you want to withdraw"))
            if userdata[0]['balance'] < amount:
                print("sorry you dont have that much money")
            else:
                userdata[0]['balance'] -= amount
                Bank._update()
                print("Amount withdraw successfully")        
    
    
    
              
print("press 1 for creating an account")
print("press 2 for depositing money in the bank")
print("press 3 for withdrawing the money")
print("press 4 for details")
print("press 5 for updating the details")
print("press 6 for deleting your account")
check=int(input("tell your response :-"))
if check == 1:
    user.Createaccount()
if check == 2:
    user.depositingmoney()
if check == 3:
    user.withdrawmoney()    
if check == 4:
    user.showdetails()
if check == 5:
    user.updatedetails()
if check == 6:
    user.deleteaccount()

          