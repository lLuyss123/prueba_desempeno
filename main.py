from funtions import *
import os
op=menu()

while op<6:
    
    if op==1:
        keep_add=True
        
        while keep_add:
            print("** Adding **")
            id=verify_id_age("id")
            name= input("Student's name: ")
            age = verify_id_age("age")
            program= input("Student's Program: ")
            csv_exist= os.path.exists(archi_name)
            if not csv_exist: 
                Metoh_Write([{
                        "id":id,
                        "name":name,
                        "age":age,
                        "program":program,
                        "state": True
                    },])
            else:
                Metoh_Adding([{
                        "id":id,
                        "name":name,
                        "age":age,
                        "program":program,
                        "state": True
                    },])
            keep_add=valid_option_to_contin()
            
                    
    elif op==2:
        Print_csv()
    elif op==3:
        op2= valid_op2()
        if op2==1:
            id= input("What's the Id: ")
            Metoh_Searching(id,None)
        else:
            name= input("What's the Name: ")
            Metoh_Searching(None,name)
        
    elif op==4:
        print("--- Updating ---")
        id=input("What's the Student id: ")
        Metoh_Updating(id)
    
    elif op==5:
        op2= valid_op2()
        if op2==1:
            id= input("What's the Id: ")
            Metoh_Deleting(id,None)
        else:
            name= input("What's the Name: ")
            Metoh_Deleting(0,name)
        
    
    #Ask for the options to the user    
    op=menu()
    
print("-------*************-------")
print("END")