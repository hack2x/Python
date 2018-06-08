Data = {}
def getUserData(name,age,phone,reg):
    in_dat = (name,age,phone)
    Data[reg] = in_dat

def printAllData():
    for k in Data:
        print("Reg: ",k,"\n",Data[k])

x='y'
while(x=='y'):
    name=input("Enter Name: ")
    age=input("Enter Age: ")
    phone=input("Enter phone: ")
    reg=input("Enter Reg: ")
    getUserData(name,age,phone,reg)
    x = input("Continue: ")

printAllData()
    
