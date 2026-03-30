#I imported the csv because I want to save the information on it 
# I imported the os module because I wanted to know if my file csv exist
import csv
import os

# File's name
archi_name= "studens.csv"

#Function that show the options AND it will repeat until the user select a valid option
def menu ():
    is_ok = True
    print("----- Option's Menu ----- \n 1. Add new Student \n 2. Show Student's list \n 3. Search Student \n 4. Update Student's info \n 5. Delete Student \n 6. Exit " )
    while is_ok:
        try:
            op = int(input("Selecct an Option: "))
            if op > 0 and op < 7:
                is_ok = False
                return op
            else:
                print("Options 1 to 6 only")
        except:
            print("Option not valid*")

#Function that show the options AND it will repeat until the user select a valid option
def valid_option_to_contin():
    is_ok = False
    while is_ok == False:
        value = input("Do you want to keep adding items (YES/NO): ").lower().strip()
        if value == "no":
            return False
        elif value == "yes":
            return True
        else:
            print("Only Yes or No")

#Metoh get id, I open the file csv and I read it then I put the info into a List
def Metoh_getid():
    lis=[]
    with open (archi_name, mode="r") as file:
        reader= csv.DictReader(file)
        for dic in reader:
            lis.append(dic["id"]) 
    return lis  


#Metoh that verify the id and the age when I enter data to the csv that the reason I need to verify the id is not on the csv so I can add the Student.
def verify_id_age(info):
    is_ok = True
    csv_exist= os.path.exists(archi_name)
    if info =="id":
        while is_ok:
            try:
                id = int(input("Student Id: "))
                if id > 0:
                    if not csv_exist:
                        is_ok = False
                        return id
                    else:
                        lis=Metoh_getid()
                        find=False
                        for lisid in lis:
                            if int(lisid) == id:
                                find=True
                                print("The Previews Id is already used")
                        if find == False:
                            is_ok = False
                            return id
                else:
                    print("Id has to be > 0")
            except:
                print("Id is not Valid")
                
    if info =="age":
        while is_ok:
            try:
                age = int(input("Student Age: "))
                if age > 0:
                    is_ok = False
                    return age
                else:
                    print("Age has to be > 0")
            except:
                print("Age is not Valid")
    

# Verify the state and will repeact until the user enter a value option
def verify_state():
    is_ok=True
    while is_ok:
        state=input("Is the Student Active?  Yes or No: ").strip().lower()
        if state == "yes":
            is_ok=False
            return True
        elif state == "no":
            is_ok=False
            return False
        else:
            print("The option is not valid")
            
    

# Verify the state and will repeact until the user enter a value option
def valid_op2(info):
    is_ok = False
    while is_ok == False:
        value = input(f"{info} by \n 1. Id \n 2. Name \n : ").lower().strip()
        if value == "1" or value =="id":
            is_ok = True
            return 1
        elif value == "2" or value =="name":
            is_ok = True
            return 2
        else:
            print("Option not valid")





# CSV CSV CSV  CSV CSV CSV  CSV CSV CSV   CSV CSV CSV  CSV CSV CSV  CSV CSV CSV  CSV CSV CSV  CSV CSV CSV  CSV CSV CSV  CSV


# #Metoh Write
# I use this function to add to the inventory for the 1st time as well I use it when I need to delet or update 1 student on the csv 
def Metoh_Write(lis):
        with open (archi_name, mode="w",newline="") as file:
            writer= csv.DictWriter(file,fieldnames=["id","name","age","program","state"])
            writer.writeheader()
            for dic in lis:
                writer.writerow(
                    dic
                )
  


#Metoh get Header
#I use this function just to know what are the field names of the csv
def Metoh_getheader():
    with open (archi_name, mode="r") as file:
        reader= csv.DictReader(file)
        header= reader.fieldnames
        return header
    
        
#Metoh Print CSV
# To show de csv 
def Print_csv():
    with open (archi_name, mode="r") as file:
        reader= csv.DictReader(file)
        for dic in reader:
            line=""
            for k,v in dic.items():
                line+= f"{k}: {v}  " 
            print(line)
        
#Metoh Adding 
#To add into the csv when it has students 
def Metoh_Adding(lis):
    with open (archi_name, mode="a",newline="") as file:
        add= csv.DictWriter(file,fieldnames=Metoh_getheader())
        for dic in lis:
                add.writerow(
                    dic
                )

#Metoh Searching 
#I Search by id or name and I dont need to change id to int because its a string and the id on the csv is a string too
def Metoh_Searching(id=None,name=None):
    find=False
    with open (archi_name, mode="r") as file:
        reader= csv.DictReader(file)
        for dic in reader:
            if name is not None or id is not None:
                if  dic["id"]==id:
                    find=True
                    line=""
                    for k,v in dic.items():
                        line += f"{k}: {v}  "
                    print(line)
                if  dic["name"]==name:
                    find=True
                    line=""
                    for k,v in dic.items():
                        line += f"{k}: {v}  "
                    print(line)
        if find ==False:
            print("Student were not find")   
                    
#Metoh Deleting 
#I Deleat by id or name and I dont need to change id to int because its a string and the id on the csv is a string too
def Metoh_Deleting(id=None,name=None):
    lista=[]
    find=False
    with open (archi_name, mode="r") as file:
        reader= csv.DictReader(file)
        
        for dic in reader:
            if  dic["name"]==name or dic["id"]==id:
                find=True
                continue    
            lista.append(dic) 
    Metoh_Write(lista)
    if find:
        print("----- DELETED -----")
    else:
        print("Not Found")
    

#Metoh Updating 
#I Update by id and I dont need to change id to int because its a string and the id on the csv is a string too
def Metoh_Updating(id):
    lista=[]
    find=False
    with open (archi_name, mode="r") as file:
        reader= csv.DictReader(file)
        
        for dic in reader:
            if dic["id"]== id:
                print(f"Previews info: {dic}")
                find=True
                name= input("New Name: ")
                age = verify_id_age("age")
                program= input("New Progam: ")
                state=verify_state()
                lista.append({
                    "id":id,
                    "name":name,
                    "age":age,
                    "program":program,
                    "state": state
                })
                continue
            lista.append(dic)    
    Metoh_Write(lista)
    if find:
        print("+++++ UPDATED ++++++")
    else:
        print("Not Found")
                
            