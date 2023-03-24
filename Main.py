import NotMain

def GetChoice():
    print("Enter your choice for what you need to do with the database.. \n1-'input' Input an entry \n2-'read' See all the entries \n3- 'exit' to halt the program ")
    choice = input("Your choice: ")
    if choice == "input":
        NotMain.DataInput()
    if choice == "read":
        NotMain.DataOutput()
    if choice == "exit":
        return
    else:
        GetChoice()
GetChoice()