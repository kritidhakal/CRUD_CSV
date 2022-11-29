import csv
import os
options = input("what do u wanna do signup(s) or login(l) or delete(d) or update(u)?")
match options:
    case "s":
        name = input("Your name please!")
        email = input("Your email id please!")
        id = input("Your id please!")

        def saveToReg(name, email, id):
            with open('register.csv', 'a', newline='') as regfile:
                header = ['Name', 'Email', 'Id']
                csv_writer = csv.DictWriter(regfile, fieldnames=header)
                csv_writer.writerow({'Name': name, 'Email': email, 'Id': id})
        saveToReg(name, email, id)

    case "l":
        name = input("Your name please!")
        email = input("Your email id please!")
        id = input("Your id please!")
        def checkCred(name, email, id): 
            with open('register.csv', mode='r') as regfile:
                header = ['Name', 'Email', 'Id']
                csv_reader = csv.DictReader(regfile, fieldnames = header)
                for row in csv_reader:
                    if(row.get("Name")==name and row.get("Email")==email and row.get("Id")==id):
                        print("You are successfully logged in!!")
                        break;
                else:       
                    print("you are not")
        checkCred(name, email, id)

    case "d":
        with open('register.csv', 'r') as inp, open('updated.csv', 'w', newline="") as out:
            header = ['Name', 'Email', 'Id']
            writer = csv.DictWriter(out, fieldnames = header)
            id_val = input("enter the id of that data to be deleted: ")
            for row in csv.DictReader(inp, fieldnames = header):
                if row.get("Id") != id_val:
                    writer.writerow(row)
        os.replace('updated.csv', 'register.csv')       

    case "u":
        with open('register.csv', 'r') as inp, open('updated.csv', 'w', newline="") as out:
            header = ['Name', 'Email', 'Id']
            writer = csv.DictWriter(out, fieldnames = header)
            id_val = input("enter the id of that data to be updated: ")
            name = input("Your name please!")
            email = input("Your email id please!")
            id = input("Your id please!")
            for row in csv.DictReader(inp, fieldnames = header):
                if row.get("Id") == id_val:
                    writer.writerow({'Name': name, 'Email': email, 'Id': id})
                    continue
                writer.writerow(row)
        os.replace('updated.csv', 'register.csv')
                    





                
