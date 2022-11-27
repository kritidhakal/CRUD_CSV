import csv
options = input("what do u wanna do signup(s) or login(l) or delete(d) or update(u)?")
match options:
    case "s":
        name = input("Your name please!")
        email = input("Your email id please!")
        id = input("Your id please!")

        def saveToReg(name, email, id):
            with open('register.csv', 'a', newline='') as regfile:
                csv_writer = csv.writer(regfile)
                csv_writer.writerow([name, email, id])
        saveToReg(name, email, id)

    case "l":
        name = input("Your name please!")
        email = input("Your email id please!")
        id = input("Your id please!")
        def checkCred(name, email, id): 
            with open('register.csv', mode='r') as regfile:
                csv_reader = csv.reader(regfile, delimiter=',')
                for row in csv_reader:
                    if(row[0]==name and row[1]==email and row[2]==id):
                        print("You are successfully logged in!!")
                        break;
                else:       
                    print("you are not")
        checkCred(name, email, id)

    case "d":
        with open('register.csv', 'r') as inp, open('updated.csv', 'w') as out:
            writer = csv.writer(out)
            id_val = input("enter the id of that data to be updated: ")
            for row in csv.reader(inp):
                if row[2] != id_val:
                    writer.writerow(row)
            with open('updated.csv', 'r') as inp, open('register.csv', 'w') as out:
                writer = csv.writer(out)
                for row in csv.reader(inp):
                    writer.writerow(row)

    case "u":
        with open('register.csv', 'r') as inp, open('updated.csv', 'w') as out:
            writer = csv.writer(out)
            id_val = input("enter the id of that data to be updated: ")
            name = input("Your name please!")
            email = input("Your email id please!")
            id = input("Your id please!")
            for row in csv.reader(inp):
                if row[2] == id_val:
                    writer.writerow([name, email, id])
                    continue
                writer.writerow(row)
        with open('updated.csv', 'r') as inp, open('register.csv', 'w') as out:
            writer = csv.writer(out)
            for row in csv.reader(inp):
                writer.writerow(row)